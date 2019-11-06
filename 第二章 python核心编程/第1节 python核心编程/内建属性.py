class ItCast(object):
    def __init__(self, obj):
        self.subject1 = obj
        self.subject2 = 'obj'

    # 在访问类的属性的时候会调用这个方法   特别注意 不能再这个方法中调用self.属性  否则会死循环
    def __getattribute__(self, item):
        if item == "subject1":
            print("log subject1")
            return 'redirect python'
        else:
            return object.__getattribute__(self, item)


it = ItCast("python")
print(it.subject1)
# log subject1
# redirect python
print(it.subject2)
# obj
