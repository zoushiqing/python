import os

pid = os.fork()
if pid == 0:
    print("子进程----")
else:
    print("父进程----")

pid = os.fork()
if pid == 0:
    print("子进程1----")
else:
    print("父进程2----")

    # 父进程----
    # 父进程2----
    # 子进程----
    # 子进程1----
    # 父进程2----
    # 子进程1----
'''
 

'''
