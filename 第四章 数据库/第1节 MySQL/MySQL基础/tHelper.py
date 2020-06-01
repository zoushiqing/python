# coding=utf-8
from MySqlHelper import MysqlHelper

# 修改
# name = raw_input("请输入学生姓名")
# id1 = raw_input("请输入学生编号")
#
# sql = 'update students set name =%s where id=%s'
# params = [name, id1]
# sqlHelper = MysqlHelper(host='127.0.0.1', port=3306, user='root', passwd='z15201384515', db='python3',
#                         charset='utf8')
# sqlHelper.cud(sql, params)

# 查询
sql = 'select * from students where id < 5'
sqlHelper = MysqlHelper(host='127.0.0.1', port=3306, user='root', passwd='z15201384515', db='python3',
                        charset='utf8')
result = sqlHelper.all(sql)
print result
