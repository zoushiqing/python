def w1(func):
    def inner():
        print("--执行了w1装饰方法inner--")
        return "w1--" + func()

    return inner


def w2(func):
    def inner():
        print("--执行了w2装饰方法inner--")
        return "w2--" + func()

    return inner


@w1
@w2
def fun1():
    return "---fun1---"


def fun2():
    return "---fun2---"


print(fun1())

''''
装饰的时候从上到下 执行
调用的时候 从下到上执行
'''


# 参数
# def func(functionName):
#     print("func----1")
#
#     def fun_in(*args, **kwargs):
#         print("fun_in----1")
#         functionName(*args, **kwargs)
#         print("fun_in----2")
#
#     print("func----2")
#     return fun_in
#
#
# @func
# def test(a, b):
#     print("test---", a, b)
#
#
# test(1, 2)

# 返回值
def func(functionName):
    def fun_in(*args, **kwargs):
        return functionName(*args, **kwargs)

    return fun_in


@func
def test():
    return "args"


print(test())
