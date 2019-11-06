class Person():
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person("老王", 1000)
laozhao = Person("老赵", 2000)
# 这就是对象动态添加属性   如果再新new一个对象是不会有这个属性的  也就是laozhao不会有这个属性
laowang.addr = "成都"
print("%s  %d  %s" % (laowang.name, laowang.age, laowang.addr))
print("{0} {1} {2}".format(laowang.name, laowang.age, laowang.addr))

# 给类添加属性  点添加了 都会有这个属性
Person.num = 1000
print(laowang.num)
laozhao = Person("老赵", 2000)
print(laozhao.num)

# 添加方法
import types


def run(self):
    print("--开始跑--{0}-".format(self.name))


laowang.run = types.MethodType(run, laowang)
laowang.run()


# 添加静态方法
@staticmethod
def go():
    print("--静态方法")


Person.go = go
Person.go()


# 添加类方法
@classmethod
def go1():
    print("--类方法")


Person.go1 = go1
Person.go1()


# 禁止添加字段 如果没有这个属性的话  就会报错
class Foo:
    # name 和 age 属性不能动态添加
    __slots__ = ("name", "age")
