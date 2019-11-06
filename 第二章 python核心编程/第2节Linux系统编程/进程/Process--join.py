from multiprocessing import Process
import time


def test():
    for i in range(5):
        print("test", i)
        time.sleep(1)


p = Process(target=test)
p.start()
# 有了这个  main进程就会等待子进程 执行完成之后  再会执行main  如果不添加就会先把main打印出来
p.join(1)  # 参数是等待的超时时间
# p.terminate()   立即结束这个进程
print("main---")
