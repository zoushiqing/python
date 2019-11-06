'''
Raise语句抛出一个指定的异常 Raise NameError('hiThere')
raise唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者异常的类
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么简单的一个raise语句就能将它再次抛出

'''
import sys

try:
    f = open('myFile.txt')
    s = f.readline()
    i = s.strip()
except OSError as err:
    print("{0}".format(err))
except ValueError:
    print("fadsfd")
except:
    print("fasdfasd")
    raise
finally:
    print("执行了Finn")
