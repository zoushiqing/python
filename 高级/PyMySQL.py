import pymysql

# 打开数据库
db = pymysql.connect("localhost", "root", "z15201384515", "runoob_db")
# 使用cursor方法创建一个cusor游标对象cursor
cursor = db.cursor()
# 使用execute方法执行sql查询
cursor.execute("SELECT VERSION()")
# 使用fetchone方法查询单条数据
data = cursor.fetchone()
print("DataBase version is {}".format(data))
# 关闭数据库连接
db.close()
