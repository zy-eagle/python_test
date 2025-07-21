from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import urllib.request

URLS = [
    'http://www.baidu.com',
    'http://www.baidu.com',
    'http://www.baidu.com',
    'http://www.baidu.com',
    'http://www.baidu.com',
    'http://www.baidu.com',
]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

with ThreadPoolExecutor(max_workers=2) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f"{url} generated an exception: {exc}")
        else:
            print(f"{url} page length: {len(data)}")