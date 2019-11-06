# coding=utf-8
'''
函数代码块以def开头，后接函数标识符名称和圆括号（）
任何传入参数和自变量必须方法在（）内，云括号之间可以用于定义参数
函数以冒号开始，并且缩进
return结束函数，选择性的返回一个值给调用方。

'''


def area(width, height):
    return width * height


print area(100, 200)


def print_welcome(name):
    print name


print_welcome("红色警戒军军")


# 必须参数
def preme(str):
    print str
    return


preme("heloo")
# 关键字参数
preme(str="helloworld")

'''
不定长参数
加了* 的参数会以元祖的形式导入，存放所有未命名的变量参数
两个* 是以字典的形式传入
'''


def printInfo(arg1, *vartuple):
    print arg1
    print vartuple


printInfo(12, 23, 43, 42, 42, 5)


def printDic(arg1, **varDic):
    print arg1
    print varDic


printDic(1, a=1, b=2)
'''
匿名函数
lambda表达式
'''
sum = lambda a, b: a + b
print sum(3, 4)

