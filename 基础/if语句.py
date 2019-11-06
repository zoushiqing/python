# encoding=utf-8
if -1:
    print ("我是-1")
else:
    print ("没有执行-1")

if 0:
    print ("我是0")
else:
    print ("没有执行0")
if 1:
    print ("我是1")
else:
    print ("没有执行1")
'''
综上：当是0的时候是false   当-1 或者 1 的时候是true


'''

num = int(input("输入一个数字"))
if num % 2 == 0:
    if num % 3 == 0:
        print ("可以整除2和3")
    else:
        print ("可以整除2 不可以整除3")
else:
    if num % 3 == 0:
        print ("不可以整除2 可以整除3")
    else:
        print ("不可以整除 2 和 36")
