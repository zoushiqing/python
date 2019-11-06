from threading import Thread
import time

num = 100


def work1():
    for i in range(5):
        # 要修改全局变量就得加个global
        global num
        num += 1
    print("work1 执行完毕: ", num)


def work2():
    print("work2 执行完毕：", num)


t1 = Thread(target=work1)
t1.start()
# 延时⼀会，保证t1线程中的事情做完
time.sleep(1)
t2 = Thread(target=work2)
t2.start()
# work1 执行完毕:  105
# work2 执行完毕： 105
'''

'''
