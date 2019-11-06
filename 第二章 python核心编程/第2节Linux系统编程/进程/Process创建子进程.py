from multiprocessing import Process
import time

'''
os.fork() 的方式创建进程是不能跨平台的  只能来 Linux  unix mac 不能再windows中用  以后代码不再使用这种方式
from multiprocessing import Process   这种方式能跨平台
'''
'''
这种方式：主进程：会等待子进程执行完成之后才会结束
'''


def test():
    while True:
        print("test")
        time.sleep(1)


p = Process(target=test)
p.start()  # 启动这个进程

while True:
    print("main")
    time.sleep(1)
