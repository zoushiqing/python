# coding=utf-8
def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b
    print


def fibo2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


'''
一个模块被另一个模块第一次引入 的时候，其主程序将被执行。如果我们想在模块被引入时，模块中的某一个程序块不执行，这时候可以用__name__来使
该程序仅在自身模块运行时执行。
每一个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是其他模块在引入。
'''
if __name__ == '__main__':
    print("程序自身运行")
else:
    print("我来子另一模块")
