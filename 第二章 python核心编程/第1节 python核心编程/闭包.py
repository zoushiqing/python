def test(number):
    def test_in(number_in):
        print("test_in", number_in)
        return number + number_in

    return test_in


print(test(10)(100))

'''
在函数的里面 定义了一个函数  里面的函数调用了外面函数的变量：里面函数和外面函数的变量共同称为闭包
'''


def line_area(width, height):
    def area(arg):
        return (width + height) * arg

    return area


line = line_area(100, 200)
print(line(2))
print(line(3))


