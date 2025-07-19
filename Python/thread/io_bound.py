# io_bound_thread_vs_single.py
import threading
import time
import requests

URLS = ["https://httpbin.org/delay/2" for _ in range(5)]

def fetch(url):
    response = requests.get(url)
    print(f"{url} 응답 완료")

# 단일 루프 실행
start = time.time()
for url in URLS:
    fetch(url)
end = time.time()
print("[단일 루프] Time taken:", end - start, "seconds")

# 쓰레드 실행
start = time.time()
threads = [threading.Thread(target=fetch, args=(url,)) for url in URLS]
for t in threads: t.start()
for t in threads: t.join()
end = time.time()
print("[쓰레드] Time taken:", end - start, "seconds")
