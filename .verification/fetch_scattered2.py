import sys, re, time, json
sys.stdout.reconfigure(encoding='utf-8')
from curl_cffi import requests as r
from urllib.parse import urljoin

URLS_TRY = [
    # Try multiple known DOJ slugs and Wayback first
    ('wayback', 'https://archive.org/wayback/available?url=https://www.justice.gov/usao-cdca/pr/five-alleged-members-foreign-based-cyber-criminal-group-charged-cybercrime-attacks'),
    ('wayback', 'https://archive.org/wayback/available?url=https://www.justice.gov/opa/pr/five-members-international-cyber-criminal-group-charged-cybercrime-attacks-multiple'),
    ('direct', 'https://www.justice.gov/usao-cdca/pr/five-alleged-members-foreign-based-cyber-criminal-group-charged-cybercrime-attacks'),
]


def akamai_solve(session, url, html):
    bm_match = re.search(r'"bm-verify"\s*:\s*"([^"]+)"', html)
    i_match = re.search(r'var i = (\d+);', html)
    n_match = re.search(r'Number\("(\d+)" \+ "(\d+)"\)', html)
    if bm_match and i_match and n_match:
        bm_verify = bm_match.group(1)
        pow_value = int(i_match.group(1)) + int(n_match.group(1) + n_match.group(2))
        verify_url = urljoin(url, '/_sec/verify?provider=interstitial')
        payload = json.dumps({'bm-verify': bm_verify, 'pow': pow_value})
        print('[akamai] solving with pow', pow_value, flush=True)
        resp = session.post(verify_url, data=payload, impersonate='chrome124',
                            headers={'Content-Type':'application/json','Referer':url}, timeout=30)
        print('[akamai verify status]', resp.status_code, resp.text[:200], flush=True)
        try:
            data = resp.json()
        except Exception:
            return None
        loc = data.get('location')
        if loc:
            return urljoin(url, loc)
    # try meta-refresh
    m = re.search(r'<meta[^>]*http-equiv=["\']refresh["\'][^>]*content=["\'][^"\']*url=([^"\']+)', html, re.I)
    if m:
        nu = m.group(1)
        return urljoin(url, nu) if not nu.startswith('http') else nu
    return None


def fetch_direct(url, max_iter=3):
    s = r.Session()
    cur = url
    for i in range(max_iter):
        resp = s.get(cur, impersonate='chrome124', timeout=30)
        print(f'  iter{i} status={resp.status_code} len={len(resp.text)}', flush=True)
        if resp.status_code == 200 and len(resp.text) > 8000:
            return resp.status_code, resp.text
        if resp.status_code in (200, 403) and len(resp.text) < 8000:
            nxt = akamai_solve(s, cur, resp.text)
            if not nxt:
                # just sleep + retry
                time.sleep(5.5)
                resp2 = s.get(cur, impersonate='chrome124', timeout=30, headers={'Referer': cur})
                print(f'  retry status={resp2.status_code} len={len(resp2.text)}', flush=True)
                if resp2.status_code == 200 and len(resp2.text) > 8000:
                    return resp2.status_code, resp2.text
                cur = cur  # try once more
            else:
                time.sleep(2)
                cur = nxt
        else:
            return resp.status_code, resp.text
    return resp.status_code, resp.text


def fetch_wayback(api_url):
    s = r.Session()
    resp = s.get(api_url, impersonate='chrome124', timeout=30)
    if resp.status_code != 200:
        return None
    try:
        data = resp.json()
    except Exception:
        return None
    snap = data.get('archived_snapshots',{}).get('closest')
    if not snap or snap.get('status') != '200':
        return None
    snap_url = snap['url']
    print('[wayback closest]', snap_url, flush=True)
    resp2 = s.get(snap_url, impersonate='chrome124', timeout=45)
    return resp2.status_code, resp2.text, snap_url


for kind, url in URLS_TRY:
    print(f'=== {kind}: {url} ===', flush=True)
    try:
        if kind == 'wayback':
            res = fetch_wayback(url)
            if not res:
                print('no wayback snap')
                continue
            status, html, snap_url = res
            print(f'STATUS: {status} LEN: {len(html)}', flush=True)
            if status == 200 and len(html) > 8000:
                with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_url.txt', 'w', encoding='utf-8') as f:
                    f.write(snap_url)
                print('[saved wayback]', snap_url)
                sys.exit(0)
        else:
            status, html = fetch_direct(url)
            print(f'final status={status} len={len(html)}', flush=True)
            if status == 200 and len(html) > 8000:
                with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html','w',encoding='utf-8') as f:
                    f.write(html)
                with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_url.txt','w',encoding='utf-8') as f:
                    f.write(url)
                print('[saved direct]', url)
                sys.exit(0)
    except Exception as e:
        print('ERROR:', e)

print('[FAIL ALL]')
sys.exit(1)
