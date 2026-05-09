import sys, re, time
sys.stdout.reconfigure(encoding='utf-8')
from curl_cffi import requests as r

URL_PRIMARY = 'https://www.justice.gov/opa/pr/five-members-international-cyber-criminal-group-charged-cybercrime-attacks-multiple'
URL_FALLBACK1 = 'https://www.justice.gov/usao-cdca/pr/five-alleged-members-foreign-based-cyber-criminal-group-charged-cybercrime-attacks'
URL_FALLBACK2 = 'https://www.justice.gov/opa/pr/charges-against-five-alleged-members-international-cyber-criminal-group'


def fetch(url: str) -> tuple[int, str]:
    s = r.Session()
    resp = s.get(url, impersonate='chrome124', timeout=30)
    text = resp.text
    if resp.status_code == 200 and len(text) < 8000:
        # Akamai bm-verify challenge
        m = re.search(r'<meta[^>]*http-equiv=["\']refresh["\'][^>]*content=["\'][^"\']*url=([^"\']+)', text, re.I)
        if m:
            next_url = m.group(1)
            if not next_url.startswith('http'):
                from urllib.parse import urljoin
                next_url = urljoin(url, next_url)
            print(f'[challenge detected] meta-refresh -> {next_url}', flush=True)
            time.sleep(5.5)
            resp2 = s.get(next_url, impersonate='chrome124', timeout=30, headers={'Referer': url})
            return resp2.status_code, resp2.text
        # try wait and refetch same URL
        if 'bm-verify' in text or 'Akamai' in text:
            print('[bm-verify cookie set, retrying]', flush=True)
            time.sleep(5.5)
            resp2 = s.get(url, impersonate='chrome124', timeout=30, headers={'Referer': url})
            return resp2.status_code, resp2.text
    return resp.status_code, text


for url in [URL_PRIMARY, URL_FALLBACK1, URL_FALLBACK2]:
    print(f'=== Trying: {url} ===', flush=True)
    try:
        status, html = fetch(url)
        print(f'STATUS: {status}  LEN: {len(html)}', flush=True)
        if status == 200 and len(html) > 8000:
            out = open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html', 'w', encoding='utf-8')
            out.write(html)
            out.close()
            with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_url.txt', 'w', encoding='utf-8') as fu:
                fu.write(url)
            print(f'[saved] from {url}')
            sys.exit(0)
    except Exception as e:
        print(f'ERROR: {e}')
        continue

print('[FAIL] all URLs failed')
sys.exit(1)
