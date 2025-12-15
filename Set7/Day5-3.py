import threading
import time

semaphore = threading.Semaphore(3)

def api_call(i):
    with semaphore:
        print(f"Thread {i} making API call")
        time.sleep(2)
        print(f"Thread {i} finished")

threads = []

for i in range(15):
    t = threading.Thread(target=api_call, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    print("Fetching - ",threading.currentThread().name,url)

urls = ["a.com", "b.com", "c.com"]

with ThreadPoolExecutor(max_workers=3) as exe:
    exe.map(fetch, urls)
