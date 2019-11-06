'''
命名空间查找顺序：
局部的命名空间->全局命名空间->内置命名空间

无法从外部命名空间去访问内部命名空间的成员


python 中只有model，class,函数(def,lambda)才回引入新的作用域，其他的代码块(如 if/else/elif,try/excpet,for/while等
都不会引入新的作用域) 也就是这些语句内定义的变量，外部是可以访问的

'''
# 这是一个全局变量
total = 0


def sum(arg1, arg2):
    # 返回两个参数的和
    total = arg1 + arg2
    print("函数内是局部变量：", total)
    return total


sum(10, 20)
print("函数外是全局变量", total)
# 函数内是局部变量： 30
# 函数外是全局变量 0


'''
当内部作用域想修改外部作用域的时候，就要用到global和nonlocal关键字
'''
num = 1


def func1():
    global num  # 需要使用global关键字声明
    num = 2
    print(num)


func1()
print(num)


# 2
# 2


def outer():
    num = 100

    def inner():
        nonlocal num  # 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
        num = 200
        print(num)

    inner()
    print(num)


outer()
# 200
# 200

a = 10


def test():
    global a
    a = a + 1  # 声明全局 或者 通过参数传递  否则编译不通过
    print(a)


test()
