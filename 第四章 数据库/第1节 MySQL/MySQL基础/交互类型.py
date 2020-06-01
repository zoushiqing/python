# coding=utf-8
import pymysql
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='z15201384515', db='python3',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("select * from students")
    print (cur.fetchall())

    name = raw_input("请输入用户名姓名")
    insert_data = "insert into students(name) values(%s)"
    cur.execute(insert_data, [name])

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
