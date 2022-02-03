import pymysql as sql
def connection():
    db = sql.connect(host="localhost",port=3306,user="root",password="root",db="student")
    cmd = db.cursor()
    return (db, cmd)
