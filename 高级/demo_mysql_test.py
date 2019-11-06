import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="z15201384515",  # 数据库密码
# )

# print(mydb)

# "-------创建数据库---------"
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")

# "---------输出所有数据库-------"
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# "---------创建数据表-------"
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="z15201384515",  # 数据库密码
    database="runoob_db"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE sites1 (name VARCHAR(255), url VARCHAR(255))")
# 查看数据表是否存在
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# "---------主键设置-------"
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# "---------插入数据-------"
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)

# mydb.commit()  # 数据表内容有更新，必须使用到该语句

# print(mycursor.rowcount, "记录插入成功。")

# "---------批量插入-------"
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "记录插入成功。")

# "---------数据记录插入后，获取该记录的 ID -------"
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 条记录已插入, ID:", mycursor.lastrowid)

# "---------查询数据-------"
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)
# "---------创建数据表-------"
