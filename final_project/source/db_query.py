import pymysql
from datetime import datetime

class db:
    def __init__(self):
        self.host = '192.168.10.37'
        self.user = 'root'
        self.password = 'ini6223'
        self.db = 'redis_project'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8')

    def select(self, table, column, where_clause=None, order_by=None):
        conn = self.conn
        curs = conn.cursor(pymysql.cursors.DictCursor)

        if where_clause != None and order_by != None:
            sql = "SELECT %s FROM %s WHERE %s ORDER BY %s" % (column, table, where_clause, order_by)
        elif where_clause != None and order_by == None:
            sql = "SELECT %s FROM %s WHERE %s" % (column, table, where_clause)
        elif where_clause == None and order_by != None:
            sql = "SELECT %s FROM %s ORDER BY %s" % (column, table, order_by)
        else:
            sql = "SELECT %s FROM %s" % (column, table)

        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()

        return rows


    def insert_contents(self, table, cid, file_name):
        conn = self.conn
        curs = conn.cursor()

        #get a level of zero count
        level = db.select(self, 'level', 'content_level', 'min_counts=0')[0]['content_level']

        #value의 순서는 cid, content_level, file_name, generate_time, update_time
        values = "(%s, '%s', '%s', now(), null)" % (cid, level, file_name)
        sql = "INSERT INTO %s VALUES %s" % (table, values)

        curs.execute(sql)
        conn.commit()
        rowcount = curs.rowcount
        curs.close()

        return rowcount


    def update_level(self, cid, content_level):
        conn = self.conn
        curs = conn.cursor()

        sql = "UPDATE contents SET content_level = '%s', update_time = now() WHERE cid = '%s'" % (content_level, cid)

        curs.execute(sql)
        conn.commit()
        rowcount = curs.rowcount
        curs.close()

        return rowcount


    def check_max_count(self, count):
        conn = self.conn
        curs = conn.cursor()

        current_max_count = db.select(self, 'level', 'max(max_counts)')[0]['max(max_counts)']

        if current_max_count >= count:
            return True
        else:
            sql = "UPDATE level SET max_counts = '%s' WHERE max_counts = '%s'" % (count, current_max_count)
            curs.execute(sql)
            conn.commit()
            return True
