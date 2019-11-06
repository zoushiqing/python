# coding=utf-8
import sys
from 基础 import support
# 这个方法不会将整个fibo导入进来，只会将里面的对应函数导入进来
from 基础.fibo import fibo

for i in sys.argv:
    print i

print sys.path
'''
一个模块只会导入一次，不管你执行多少次import。

'''
support.print_func("老子是邹世清")

fibo(1000)

'''
dir()  可以找到模块内定义的所有名称。
'''
print dir(fibo)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__',
 '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure',
 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']


