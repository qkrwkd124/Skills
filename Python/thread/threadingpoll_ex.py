from concurrent.futures import ThreadPoolExecutor
import threading
import time

counter = 0
lock = threading.Lock()

def worker():
    global counter
    for _ in range(10000000):
        with lock:
            counter += 1

with ThreadPoolExecutor(max_workers=10) as executor:
    start = time.time()
    futures = [executor.submit(worker) for _ in range(10)]
    for f in futures:
        f.result()
    end = time.time()

print(f"Counter: {counter}")
print(f"Time taken: {end - start} seconds")