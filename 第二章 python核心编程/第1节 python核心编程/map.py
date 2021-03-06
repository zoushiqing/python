ret = map(lambda x: x * x, [1, 2, 3])  # 函数，可迭代对象
for t in ret:
    print(t)
# 1
# 4
# 9

# ---------------------------------------------------
ret_1 = map(lambda x, y: x + y, [1, 2, 3, 4], [4, 5, 6])
for t in ret_1:
    print(t)


# 5
# 7
# 9

# ---------------------------------------------------
def f1(x, y):
    return (x, y)


l1 = [11, 22, 33, 44, 55, 66]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']
l3 = map(f1, l1, l2)
print(list(l3))
# [(11, 'a'), (22, 'b'), (33, 'c'), (44, 'd'), (55, 'e'), (66, 'f')]

# ---------------------------------------------------
f = filter(lambda x: x % 2, [1, 2, 3, 4])
print(list(f))
# [1,3]

f1 = filter(None, "she")  # 不进行过滤
print(str(f1))

# ---------------------------------------------------
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)
# 15
reduce(lambda x, y: x + y, ['a', 'b', 'c', 'd'], 'e')
# 'eabcd'

# ---------------------------------------------------

a = [234, 45, 32, 23, 23, 12, 12, 5, 4, 4, 3, 2, 1, 1, 1]
sorted(a)  # [1, 1, 1, 2, 3, 4, 4, 5, 12, 12, 23, 23, 32, 45, 234]
sorted(a, reverse=True)  # [234, 45, 32, 23, 23, 12, 12, 5, 4, 4, 3, 2, 1, 1, 1]
