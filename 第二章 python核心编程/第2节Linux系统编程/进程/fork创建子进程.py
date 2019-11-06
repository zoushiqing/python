import os
import time

# 创建一个子进程  会返回两次  两个值 一个是父进程 一个是子进程
pid = os.fork()
print("pid:", pid)
# 子进程是0  父进程大于0
if pid == 0:
    while True:
        print("---子进程----{}---{}".format(os.getpid(), os.getppid()))  # 获得进程id 获得父进程id  进程id最大65535
        time.sleep(1)
else:
    while True:
        print("---父进程----{}".format(os.getpid()))
        time.sleep(1)

print("---over----")
'''
1.子进程不会因为父进程停止而停止
2.上面最后 print("---over----")  父进程和子进程都会执行
3.
'''
