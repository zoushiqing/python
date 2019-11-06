# coding=utf-8
'''
读和写文件
open(filename,mode)
mode:包括：只读，写入，追加等。这个参数不是强制性的，默认文件访问模式为只读。

'''
f = open("foo.txt", mode="w")
f.write("Python是一个非常好的语言，\n是的，的确非常好！！\n")
f.close()

f = open("foo.txt", "r")
str = f.read()
print(str)
f.close()
