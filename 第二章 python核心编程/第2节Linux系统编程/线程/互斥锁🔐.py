from threading import Thread, Lock
import time

g_num = 0


def test1():
    global g_num
    for i in range(1000000):
        # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这⾥⼀直等待到解锁为⽌
        # False表示⾮堵塞，即不管本次调⽤能够成功上锁，都不会卡在这,⽽是继续执⾏下⾯的代码
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
        mutex.release()
        print("---test1---g_num=%d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)  # True表示堵塞
        if mutexFlag:
            g_num += 1
        mutex.release()


print("---test2---g_num=%d" % g_num)
# 创建⼀个互斥锁
# 这个所默认是未上锁的状态
mutex = Lock()
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
print("---g_num=%d---" % g_num)
