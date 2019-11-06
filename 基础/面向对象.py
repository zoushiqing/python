class Complex:
    def __init__(self, realpart, imapart):
        self.r = realpart
        self.i = imapart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 3.0 -4.5
print("----------------------------------------------------------------------------------")
'''
类的方法与普通函数的只有一个特殊的区别：他们必须有一个self作为第一个参数名
slef 是类的实例
'''


def prt():
    print("普通函数")


class Test:
    def prt(self):
        print("类的方法")
        print(self.__class__)  # <class '__main__.Test'>


t = Test()
t.prt()
print("----------------------------------------------------------------------------------")


class People:
    age = 0
    name = ''
    __weight = 0  # 私有属性 外部没法 对象.属性 访问  也没有法被继承

    # 这就是传说中的构造方法
    def __init__(self, age, name, weight):
        self.age = age
        self.name = name
        self.__weight = weight

    def speak(self):
        print("{} 年龄:{} 体重: {}".format(self.name, self.age, self.__weight))


p = People(12, "Tom", 23)
p.speak()

print("----------------------------------------------------------------------------------")

'''
私有的属性无法被继承
python支持多继承

'''


class student(People):
    grad = 0

    def __init__(self, age, name, weight, grad):
        People.__init__(self, age, name, weight)
        self.grad = grad

    def speak(self):
        # print("%s 年龄:%d 体重: %d 读 %d 年级".format(self.name, self.age, self.__weight, self.grad))  ---报错
        print("{}年龄:{}  读 {} 年级".format(self.name, self.age, self.grad))


s = student(12, 'Tom', 23, 6)
s.speak()
print("---------------------------方法重写-------------------------------------------------------")


class parent:
    def myMethod(self):
        print("我是父类的方法")


class child(parent):
    def myMehod(self):
        print("我是子类的方法")


p = child()
p.myMehod()  # 子类调用自己的方法
super(child, p).myMethod()  # 子类调用父类的方法
print("---------------------------类属性和方法-------------------------------------------------------")
'''
__private_attrs:两个下划线开头，声明该属性为私有属性，不能在类的外部被调用，
__private_method():两个下划线代表私有方法
__init__
'''


class demo:
    # 构造方法 在生成对象的时候调用
    def __init__(self): pass

    # 折构函数 释放对象的时候调用
    def __del__(self): pass

    # 打印，转换
    def __repr__(self): pass

    # 按照索引赋值
    def __setitem__(self, key, value): pass

    # 按照索引取值
    def __getitem__(self, item): pass

    # 获取长度
    def __len__(self): pass

    # 比较运算
    def __cmp__(self, other): pass

    # 函数调用
    def __call__(self, *args, **kwargs): pass

    # 加运算
    def __add__(self, other): pass

    # 减运算
    def __sub__(self, other): pass

    # 乘运算
    def __mul__(self, other): pass

    # 除运算
    def __truediv__(self, other): pass

    # 求余运算
    def __mod__(self, other): pass

    # 乘方运算
    def __pow__(self, power, modulo=None): pass
