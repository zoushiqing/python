class Test:
    def __init__(self):
        self.__number = 0

    def setNumebr(self, newNumber):
        if isinstance(newNumber, int):
            self.__number = newNumber
        else:
            print("不是int类型")

    def getNumber(self):
        return self.__number

    num = property(getNumber, setNumebr)


t = Test()
t.num = 200
print(t.num)

'''
第二种方式
'''


class money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money):
        self.__money = new_money


m = money()
m.money = 100
print("money:", m.money)
