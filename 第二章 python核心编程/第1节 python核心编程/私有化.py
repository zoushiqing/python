'''
__属性    私有属性
__方法()  私有方法
__方法()__  系统的方法
私有属性  子类是无法使用的
'''

number = 100
# from 第1节 python核心编程.私有化 import *  这种方式 _number导入不进去， 但是 import 第1节 python核心编程.私有化 这种方式 是可以导入进去的
_number = 200


class Test:
    def __init__(self):
        self.__num = 100

    def setNum(self, newNumber):
        self.__num = newNumber

    def getNum(self):
        return self.__num


t = Test()
# 添加属性
# t.__num1 = 200
# print(t.__num)
t.setNum(200)
print(t.getNum())
