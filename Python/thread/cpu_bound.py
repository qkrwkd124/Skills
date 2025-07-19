import threading
import time

counter = 0
lock = threading.Lock()

def worker():
    global counter
    for _ in range(10000000):
        counter += 1

def worker2():
    global counter
    for _ in range(10000000):
        with lock:
            counter += 1

# 단일 루프 실행
counter = 0
start = time.time()
for _ in range(10):
    worker()
end = time.time()
print("[단일 루프] Counter:", counter)
print("[단일 루프] Time taken:", end - start, "seconds")

# 쓰레드 실행
counter = 0
start = time.time()
threads = [threading.Thread(target=worker2) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
end = time.time()
print("[쓰레드] Counter:", counter)
print("[쓰레드] Time taken:", end - start, "seconds")