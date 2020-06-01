# coding=utf-8
import pymysql


class MysqlHelper:

    def __init__(self, host, port, db, user, passwd, charset='urf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
            print "OK"
        except Exception, e:
            print e.message

    def all(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception, e:
            print e.message
