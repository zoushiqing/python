# encoding=utf-8
'''
迭代是python最强大的功能之一，是访问集合元素的一种方式
迭代器是一个可以记录遍历的位置的对象
迭代器对象可以从集合的第一个元素开始访问，知道所有元素被访问结束。迭代器只能向前不能向后
两个基本方法：next()和iter()
'''
list = [1, 2, 3, 4]
it = iter(list)
# print next(it)
# print next(it)
for x in it:
    print x


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
