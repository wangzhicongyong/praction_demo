
"""
condition对象可以对某些事件触发后才处理数据或执行特定的功能代码
可用于不同线程之间的通信或通知，实现更高级别的通信
"""

# condition对象支持上下文处理with语句
# wait(timeout=None)方法会释放锁，并阻塞当前线程直到超时或其他线程针对同一个condition对象调用了notify（）/notify_all()
# 每一个类的对象的实例都有一个等待集合，当在该实例上调用wait()方法后，线程都会进入到该实例的等待集合中
# 方法，被唤醒之后 当前线程会重新尝试获取锁并在成功获取锁之后结束wait()方法，然后继续执行
# wait_for(条件，timeout=None)方法阻塞当前线程直到超时或者指定条件得到满足

import time
import random
from threading import Condition, Thread

# 生产者类
class Producer(Thread):

    def __init__(self, threadname):
        # 继承父类的构造方法
        Thread.__init__(self, name=threadname)

    def run(self):
        global x
        time.sleep(random.randrange(1, 5))
        con.acquire()  # 上锁

        if x == 20:
            print('生产者在等待.......')
            con.wait()  # 阻塞等待
            print('Producer resumed')  # 生产者开始

        print('生产者', end='***')
        for i in range(20):  # 弊端是数据全部生产完之后，消费者才会唤醒，进行执行
            print(x, end=' ')
            x = x + 1
        print(x)
        con.notify_all()
        con.release()

# 消费者类
class Consumer(Thread):

    def __init__(self, threadname):
        # 继承父类的构造方法
        Thread.__init__(self, name=threadname)

    def run(self):
        global x
        time.sleep(random.randrange(1, 5))
        con.acquire()

        if x == 0:  # x=0那么消费者就无法将x做递减操作  当前线程就处于阻塞状态等待-生产者生产数据-生产者有数据了
            # 就会唤醒消费者的-等待集合里面的线程（就会接着从这里开始执行）
            print('消费者 在等待.......')
            con.wait()  # 阻塞等待—让当前线程处于等待状态
            print('Consumer resumed')  # 消费者开始工作

        print('Consumer', end='***')
        for i in range(20):
            print(x, end=' ')
            x = x - 1
        print(x)
        con.notify_all()    # 消费者对象调用condition对象
        con.release()

# 创建condition对象
con = Condition()
# 全局变量
x = 0
p = Producer('Producer')
c = Consumer('Consumer')

c.start()
p.start()

# 等待两个线程都运行结束
time.sleep(5)

c.join()
p.join()
