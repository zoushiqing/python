def getAvarage(a, b):
    result = a + b
    print("result=%d" % result)
    return result


a = 100
b = 200
c = a + b
ret = getAvarage(a, b)
print(ret)
'''
命令：
1.python -m pdb 调试.py  开启调试 
2.l(lsit)  查看源代码，箭头指向就是 要运行的代码
3.n(next)  程序走一步
4.c(continue)  程序顺序执行  遇到断点才回停止 否则不会停止一直执行
5.b(break) 9  第9行添加断点
6.clear 1  删除第1个断点
7.p(print) a 打印a的值
8.s(step) 进入到一个函数n 

'''