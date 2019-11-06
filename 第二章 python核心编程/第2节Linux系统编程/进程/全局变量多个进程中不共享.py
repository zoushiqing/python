import os
import time

g_num = 100
pid = os.fork()
if pid == 0:
    print("-----process.1-----")
    g_num += 1
    print('-----process.1-----{}'.format(g_num))
else:
    time.sleep(3)
    print("-----process.2-----")
    print('-----process.2-----{}'.format(g_num))

# -----process.1-----
# -----process.1-----101
# -----process.2-----
# -----process.2-----100

'''
1.进程里面的变量是互不影响的
2.缺点  进程与进程之间全局变量是不会共享的  
3.要解决这个问题 就需要后面学的进程间通讯
'''