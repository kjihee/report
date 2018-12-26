from flask import Flask
from flask import request
import pymysql
import json
import redis
from datetime import datetime
import requests
import db_query
app = Flask(__name__)

def get_level_from_db(post_id):
    db = db_query.db()
    table = "contents"
    column = "filename, content_level"
    where_clause = "cid=%s" % (post_id)
    return db.select(table, column, where_clause)[0]


def redis_connection():
    rc = redis.Redis(host='192.168.10.108', port=6379, db=1)
    return rc

# db 에 저장되어있는 contents_level의 기준을 받아와서 level반환
def get_target(count):
    db = db_query.db()
    level_table = db.select(table='level', column ='*' )
    for i in level_table:
        if int(i['max_counts'])>= count>= int(i['min_counts']) :
            level = i['content_level']
            return level


# db_query 모듈을 이용해서 remote db에 접속하여 update를 수행하는 함수 
def update_db_level(post_id, final_level):
    db = db_query.db()
    rowcount = db.update_level(post_id, final_level)
    #affected row 반환
    return rowcount

# post 요청이 들어온 cid와 count에 대해 db를 참조하여 redis set
@app.route('/post_sentence',methods=['POST', 'GET'])
def set_contents_redis():
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    data['target'] = get_target(int(data['count']))
    data['db_level'] = get_level_from_db(data['cid'])['content_level']
    data['filename'] = get_level_from_db(data['cid'])['filename']
    data['worker_id'] = None
    rc = redis_connection()
    if data['target'] != data['db_level']:
        data['status'] = 'update'
    else:
        data['status'] = 'done'
    rc.set(data['cid'],json.dumps(data).encode('utf-8'))
    return rc.get(data['cid'])

# redis status == done 이면 db contents table 의 contents level 변경 아니면 error message
@app.route('/update_sentence', methods=['GET','POST'])
def update_sentence():
    cid = request.form['cid']
    rc = redis_connection()
    if json.loads(rc.get(cid))['status']=="done":
       update_db_level(cid,json.loads(rc.get(cid))['target'])
       print("check done and db update success")
       return cid
    else:
       print("check content status again")
       return "check your status again"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
