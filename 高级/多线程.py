'''
多线程类似于同时执行多个线程，多线程运行有如下优点：
1.使用线程可以把占据长时间的程序中的任务放到后台去处理
2.用户界面可以更加吸引人，比如用户点击一个按钮去触发某些事件的处理，可以弹出一个进度条来展示处理的进度。
3.程序的运行速度可能加快。
4.在一些等待的任务实现上如用户输入、文件读取和网络收发数据等。线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

每一个线程都有他自己的一个程序运行的入口、顺序执行的序列和程序运行的出口。但是线程不能够独立运行，必须依存在应用程序中，由应用
程序提供多个线程执行控制。

每组线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
指令指针和堆栈指针寄存器线程上下文中最重要的两个寄存器，线程总是在进程得到上下文中运行的。这些地址都用于标志拥有线程的进程地址空间中的内存。
1.线程可以被中断、抢占
2.在其他线程正在运行时，线程可以暂时搁置
'''

''''
_thread:提供低级别、原始的线程以及一个简单的锁，相对与threading模块的功能还是有限的。
threading:除了包含_thread模块中的所有方法，还提供其他方法：
    threading.currentThread():返回当前线程变量。
    threading.enumerate():返回一个包含正在运行的线程list。正在运行时指线程启动后、结束前，不包括启动前和结束后的线程。
    threading.activeCount():返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
'''
import threading  # 线程模块
import time


def sayhi(num):
    print('running on number', num)
    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(33,))  # 生成一个线程实例
    t2 = threading.Thread(target=sayhi, args=(22,))  # 生成另一个线程实例

    t1.start()  # 启动线程
    t2.start()
    print(t1.getName())  # 获取线程名
    print(t2.getName())
    t1.join()  # 阻塞主线程，等待t1子线程执行完成后再执行后面的代码
    t2.join()  # 阻塞主线程，等待t2子线程执行完成后再执行后面的代码
    print("----------------end")

exitFlag = 0


class myThreading(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("线程开始：" + self.name)
        print_time(self.name, self.counter, 5)
        print("线程结束" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag == 0:
            threadName.exit()
        time.sleep(delay)
        print("{}:{}".format(threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThreading(1, "thread_1", 1)
thread2 = myThreading(2, "thread_2", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
