# coding=utf-8
counter = 100  # 整形变量
miles = 1000.0  # 浮点型变量
name = '字符串'  # 字符串
print counter
print miles
print name
print ("# ------------------------------------------------------------------------------------------------------")
a = b = c = 1
a, b, c = 1, 2, 'runoob'
print ("# ------------------------------------------------------------------------------------------------------")
'''
六种标准的数据类型：
Number 数字
String 字符串
List 列表
Tuple 元组
Set 集合
Dictionary 字典
'''
print ("# ------------------------------------------------------------------------------------------------------")
a, b, c, d = 20, 5.5, True, 4 + 3j
print (type(a), type(b), type(c), type(d))
print (isinstance(a, int))
'''
type 不会认为子类是一种父类类型
isInstance 会认为子类是一种父类类型
'''


class A:
    pass


class B(A):
    pass


print (isinstance(A(), A))  # True
print (type(A()) == A)  # False 不明白 不是该为True吗？
print (isinstance(B(), A))
print (type(B()) == B)
print ("# ------------------------------------------------------------------------------------------------------")
'''
1.反斜杠可以用来转义，使用r可以让反斜杠不发生转义
2.字符串可以用+运算符链接在一起，使用*重复运算符
3.Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4.Python中的字符串不可以改变
'''
print ("# ------------------------------------------------------------------------------------------------------")

'''
1.列表可以完成大多数集合类的数据结构实现。列表中的元素类型可以不同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
2.列表是写在[]之间的，用逗号分隔开的元素列表。
3.和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需新元素的新列表。
4.变量[头下表：尾下表]
'''
word = "Python"
print (word[0:2])  # 输出：Py   所以python 中的截取都是包含头不包含尾
list = ['abcd', 786, 2.23, 'ruoob', 70.2]
tinytupple = [123, 'ruoob']
print (list)  # 全部
print(list[0])
print (list[1:3])  # [786, 2.23] 包含头不包含尾
print (tinytupple * 2)
print (list + tinytupple)
'''
list写在方括号之间，用逗号隔开
2.和字符串一样，list可以被索引和切片
3.list可以使用+操作符j进行拼接
4.list中的元素是可以变的
'''

'''
字符串翻转
第一个参数-1 表示最后一个元素
第二个参数为空 表示移动到末尾
第三个参数为-1 表示逆向
'''


def reverseWords(input):
    words = input.split(" ")
    return ' '.join(words[-1::-1])


if __name__ == '__main__':
    words = "I Love runoob"
    print reverseWords(words)
print ("# ------------------------------------------------------------------------------------------------------")
'''
元祖与列表相似，不同之处在于元组中的元素不可以改变 元组写在（） 里面，元素之间用逗号隔开。
拼接  重复  截取 等和列表都是一样的 只是不能更改元素罢了
虽然元组不可以更改元素 但是他可以包含可变的对象 比如list列表作为他的元素
'''
tuple = ('abc', 768, 2.23, 'runoob', 70.2)
print (tuple[1:3])  # (768, 2.23)   这个也是包含头不包含尾
'''
tup2=(22,)一个元素的时候 需要在后面加上一个逗号
'''
print ("# ------------------------------------------------------------------------------------------------------")
'''
集合的基本功能是用来进行成员关系测试和删除重复元素
使用set{}或者{}创造集合，创造一个空集合 必须使用set{} 因为空{}使用来创造字典的
集合还可以拿来进行运算
'''
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print student
if 'Rose' in student:
    print "Rose is in student"
else:
    print 'Rose is not in student'

a = set('abcdef')
b = set('abc')
print a - b  # 差集
print a | b  # 并集
print a & b  # 交集
print a ^ b  # 不同时存在的元素
print ("# ------------------------------------------------------------------------------------------------------")
'''
字典就是java中的map
列表是有序的，字典是无序的
key必须使用不可变类型
在同一字典中，key必须是唯一的
'''
dict = {}
dict['one'] = 1
dict[2] = '2'
tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.ruoob.com'}
print dict['one']
print dict
print tinyDict
print tinyDict.keys()
print tinyDict.values()
