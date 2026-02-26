import threading, time

counter = 0

def increment():
    global counter
    for _ in range(10000):
        with threading.RLock():
            counter += 1    # NOT atomic

threads = [
    threading.Thread(target=increment),
    threading.Thread(target=increment)
]
threads[0].daemon=True
for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final counter:", counter)

def worker():
    time.sleep(3)
    print("Worker done")

t = threading.Thread(target=worker, daemon=True)  # non-daemon
t.start()

print("Main exiting")