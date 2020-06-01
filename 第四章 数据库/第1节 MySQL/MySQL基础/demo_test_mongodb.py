# coding=utf-8
import pymongo

# 创建客户端，获取连接
client = pymongo.MongoClient("mongodb://localhost:27017/")
# 切换数据库
db = client.py3
# 获取集合
stu = db.stu
# 插入数据
# stu.insert_one({'name': "张三分"})
# 更新
# stu.update_one({'name': "张三分"}, {'$set': {'name': 'abc'}})
# 删除
# stu.delete_one({'name': '张三分'})
# 查询 DESCENDING 降序  ASCENDING升序
cursor = stu.find({'age': {'$gt': 20}}).sort('_id', pymongo.DESCENDING).skip(1).limit(1)
for s in cursor:
    print s['name']
