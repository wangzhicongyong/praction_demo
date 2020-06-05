
"""
多线程执行任务
"""
from threading import Thread, Lock
from time import sleep

class DataThread(Thread):

    def __init__(self, target, args=(), kwargs={}, name=None):
        super(DataThread, self).__init__()
        self.target = target
        self.name = name
        self.args = args
        self.kwargs = kwargs

    # run方法是去执行自定义类外面的普通函数(相当于run函数来说, player函数是全局变量了)
    def run(self):
        self.target(*self.args, **self.kwargs)

# 任务函数
def get_data():
        for num in range(10):
            list01.append(num)
        lock.acquire()
        data = list01.pop()
        print(data, t.getName())   # 定义线程名来区分
        lock.release()


list01 = []
lock = Lock()
t1 = []
for i in range(2):

    t = DataThread(target=get_data, name=i)
    t1.append(t)

for t in t1:
    t.start()

for t in t1:
    t.join()
