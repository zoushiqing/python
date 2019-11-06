# 元类属性
Person = type("Person", (), {"name": "邹素清"})  # 类名   父类   属性
p = Person()
p.name


# 元类方法
def print_num(self):
    print("printNum----", self.num)


Person2 = type("Person2", (), {"printNum": print_num})

p2 = Person2()
# 动态添加属性
p2.num = 100
p2.printNum()
