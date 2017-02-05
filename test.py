import urllib
import pymysql
import time
from urllib.request import urlopen

 
 
# Open database connection

_host = 'ja-cdbr-azure-west-a.cloudapp.net'
_user = 'b777abef975cef'
_pwd = '5ed53ece'
_db = 'db-60a50c09-aa74'

_time = time.strftime('%Y-%m-%d %H:%M:%S')

db = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db,charset='utf8',autocommit=True)
 
# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("""INSERT into datarecord (time,s1,s2) values (%s,%s, %s)""", (_time, 1, 2))

db.commit()
 
 
# disconnect from server
db.close()
