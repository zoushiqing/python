class Test(object):
    # 如果没有这个直接 对象() 会报错
    def __call__(self, *args, **kwargs):
        pass

    # # 在init方法之前调用
    # def __new__(cls, *args, **kwargs):
    #     pass
    #
    # # 在对象删除时触发__del__(self),然后再删除对象自己。
    # def __del__(self):
    #     pass
    #
    # # 不知道大家再写程序是，打印一个实例化对象时，打印的其实时一个对象的地址。而通过__str__()函数就可以帮助我们打印对象中具体的属性值，或者你想得到的东西。
    # def __str__(self):
    #     pass
    #
    # # 新生对象不能 动态添加这些属性
    # __slots__ = ("haha", "hheh")


t = Test()
t()


class Test1(object):
    def __init__(self, func):
        print("执行了init---")
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("执行了call--")
        self.__func()


@Test1
def test():
    print("test---")
# 当还没执行test()方法的时候 就会调用类的init方法了
# 执行了init---

# test()
# 执行了call--
# test---
