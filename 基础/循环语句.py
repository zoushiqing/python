# encoding=utf-8
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1 到 %d 之间的和：%d" % (n, sum))

count = 0
while count < 5:
    print("%d小于5" % count)
    count += 1
else:
    print(count, "等于5")

sites = ['Badu', 'Taobao', 'Runoob', 'Google']
for site in sites:
    if site == "Runoob1":
        print("菜鸟教程")
        break
    print("循环数据" + site)
else:
    print("没有循环数据")
print("完成循环")

for i in range(5, 10, 1):
    print(i)
'''
break:可以跳出for和while循环体。如果你从for或while循环终止，任何对应的else语句不会执行
continue：跳出当前循环块中的剩余语句，进入下一个循环
'''
