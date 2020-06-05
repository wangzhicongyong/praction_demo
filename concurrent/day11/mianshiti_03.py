
"""
面试题
"""
from threading import Thread, Lock
import threading
from time import sleep
from queue import Queue

q = Queue()

for i in range(10):
    q.put(i)

# 任务函数
def job_func():
    lock.acquire()
    num = q.get()
    print(num, threading.currentThread().name)  # 区分线程
    lock.release()

lock = Lock()

while True:
    if q.empty():
        break
    t1 = Thread(target=job_func, name='a')
    t2 = Thread(target=job_func, name='b')
    t1.start()
    t2.start()
    t1.join()
    t2.join()