from multiprocessing import Pool
import os, time, random

''''
当需要创建的⼦进程数量不多时，可以直接利⽤multiprocessing中的Process
动态成⽣多个进程，但如果是上百甚⾄上千个⽬标，⼿动的去创建进程的⼯
作量巨⼤，此时就可以⽤到multiprocessing模块提供的Pool⽅法。
初始化Pool时，可以指定⼀个最⼤进程数，当有新的请求提交到Pool中时，
如果池还没有满，那么就会创建⼀个新的进程⽤来执⾏该请求；但如果池中
的进程数已经达到指定的最⼤值，那么该请求就会等待，直到池中有进程结
束，才会创建新的进程来执⾏
'''


def worker(msg):
    t_start = time.time()
    print("%s开始执⾏,进程号为%d" % (msg, os.getpid()))
    # random.random()随机⽣成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执⾏完毕，耗时%0.2f" % (t_stop - t_start))


po = Pool(3)  # 定义⼀个进程池，最⼤进程数3
for i in range(0, 10):
    # Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))
    # 每次循环将会⽤空闲出来的⼦进程去调⽤⽬标  如果超过了指定的最大数量 也会添加进去的
    # apply_async 是非堵塞的   apply是堵塞的
    po.apply_async(worker, (i,))
    # po.apply(worker, (i,))
    print("----start----")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有⼦进程执⾏完成，必须放在close语句之后   不join池中的进程不会执行
print("-----end-----")
