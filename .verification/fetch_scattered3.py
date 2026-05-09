import sys, re, time, json
sys.stdout.reconfigure(encoding='utf-8')
from curl_cffi import requests as r
from urllib.parse import urljoin

URL = 'https://www.justice.gov/usao-cdca/pr/5-defendants-charged-federally-running-scheme-targeted-victim-companies-phishing-text'

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
        print('[akamai verify status]', resp.status_code, resp.text[:300], flush=True)
        try:
            data = resp.json()
        except Exception:
            return None
        if data.get('reload'):
            return url  # same URL
        loc = data.get('location')
        if loc:
            return urljoin(url, loc)
    return None


s = r.Session()
cur = URL
for i in range(4):
    resp = s.get(cur, impersonate='chrome124', timeout=30)
    print(f'iter{i} status={resp.status_code} len={len(resp.text)}', flush=True)
    if resp.status_code == 200 and len(resp.text) > 8000:
        with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html','w',encoding='utf-8') as f:
            f.write(resp.text)
        with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_url.txt','w',encoding='utf-8') as f:
            f.write(URL)
        print('SAVED')
        sys.exit(0)
    if resp.status_code == 200 and len(resp.text) < 8000:
        nxt = akamai_solve(s, cur, resp.text)
        if nxt:
            time.sleep(5.5)
            cur = nxt
            continue
        else:
            time.sleep(5.5)
            continue
    if resp.status_code == 404:
        print('404 final')
        sys.exit(2)
    time.sleep(3)

# Try wayback as backup
print('Trying wayback...')
api = 'https://archive.org/wayback/available?url=' + URL
resp = s.get(api, impersonate='chrome124', timeout=30)
data = resp.json()
snap = data.get('archived_snapshots',{}).get('closest')
if snap and snap.get('status') == '200':
    snap_url = snap['url']
    print('wayback:', snap_url)
    resp2 = s.get(snap_url, impersonate='chrome124', timeout=45)
    if resp2.status_code == 200 and len(resp2.text) > 8000:
        with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html','w',encoding='utf-8') as f:
            f.write(resp2.text)
        with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_url.txt','w',encoding='utf-8') as f:
            f.write(URL + '\nWAYBACK: ' + snap_url)
        print('SAVED via wayback')
        sys.exit(0)

print('FAIL')
sys.exit(1)
