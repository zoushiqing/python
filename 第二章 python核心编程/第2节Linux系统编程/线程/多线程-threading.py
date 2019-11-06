from threading import Thread
import time


def test():
    print("----昨晚喝多了----")
    time.sleep(1)


# 线程的执行顺序是无序的
for i in range(5):
    t = Thread(target=test)
    t.start()


# -------------------------继承Thread-----------------------------------------------------------------
class MyThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("I am is ", i)


my_thread = MyThread()
my_thread.start()

''''
1. 每个线程⼀定会有⼀个名字，尽管上⾯的例⼦中没有指定线程对象的
name，但是python会⾃动为线程指定⼀个名字。
2. 当线程的run()⽅法结束时该线程完成。
3. ⽆法控制线程调度程序，但可以通过别的⽅式来影响线程调度的⽅式。
4. 线程的⼏种状态
'''