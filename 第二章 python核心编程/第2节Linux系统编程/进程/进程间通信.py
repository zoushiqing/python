from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执⾏的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执⾏的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    # ⽗进程创建Queue，并传给各个⼦进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动⼦进程pw，写⼊:
    pw.start()
    # 等待pw结束:
    pw.join()
    # 启动⼦进程pr，读取:
    pr.start()
    pr.join()
    # pr进程⾥是死循环，⽆法等待其结束，只能强⾏终⽌:
    print('所有数据都写⼊并且读完')

# Put A to queue...
# Put B to queue...
# Put C to queue...
# Get A from queue.
# Get B from queue.
# Get C from queue.
# 所有数据都写⼊并且读完
# ----------------------------------线程池中使用Queue-------------------------------------------------------------
# 修改import中的Queue为Manager
from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print("reader启动(%s),⽗进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),⽗进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "dongGe":
        q.put(i)


if __name__ == "__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue()  # 使⽤Manager中的Queue来初始化
    po = Pool()
    # 使⽤阻塞模式创建进程，这样就不需要在reader中使⽤死循环了，可以让writer完全执⾏完成后，再⽤reader去读取
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())
