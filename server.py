import threading
import datetime
import requests, json
import time
import schedule

import urllib
import pymysql
from urllib.request import urlopen

import daemon
    

def funcTimer():

    # 1 서울 데이터.
    _tm = str (GetPost(37.5714,126.9658))
    print("##MDMonitor : Seoul : " + _tm)
    insertData(1,_tm)
    time.sleep(1)

    # 2 인천
    _tm = str (GetPost(37.4561057,126.7052611))
    print("##MDMonitor : Incheon : " + _tm)
    insertData(2,_tm)
    time.sleep(1)

    # 3 경기 남부 데이터, 수원시
    _tm = str (GetPost(37.2430863,127.0089135))
    print("##MDMonitor : KyungGiSuwon : " + _tm)
    insertData(3,_tm)
    time.sleep(1)
    
    # 4 강원도 속초 시청
    _tm = str (GetPost(38.2046487,128.5710904))
    print("##MDMonitor : GanwondoSokCho : " + _tm)
    insertData(4,_tm)
    time.sleep(1)
    
    # 5 강원도 삼척 시청
    _tm = str (GetPost(37.4435487,129.1467404))
    print("##MDMonitor : GangwonSamcheok : " + _tm)
    insertData(5,_tm)
    time.sleep(1)
    
    # 6 충북
    _tm = str (GetPost(36.6354049,127.489273))
    print("##MDMonitor : Chungbook : " + _tm)
    insertData(6,_tm)
    time.sleep(1)

    # 7 대전
    _tm = str (GetPost(36.350412,127.384547))
    print("##MDMonitor : Daecheon : " + _tm)
    insertData(7,_tm)
    time.sleep(1)
    
    # 8 전북
    _tm = str (GetPost(35.7223842,125.8176828))
    print("##MDMonitor : JeonBook : " + _tm)
    insertData(8,_tm)
    time.sleep(1)

    # 9 전남
    _tm = str (GetPost(34.8144255,126.4595968))
    print("##MDMonitor : JeonNam : " + _tm)
    insertData(9,_tm)
    time.sleep(1)

    # 10 광주시
    _tm = str (GetPost(35.1600765,126.851297))
    print("##MDMonitor : GwankJoo : " + _tm)
    insertData(10,_tm)
    time.sleep(1)

    # 11 경북
    _tm = str (GetPost(36.576111,128.5057068))
    print("##MDMonitor : KyungBook : " + _tm)
    insertData(11,_tm)
    time.sleep(1)

    # 12 대구
    _tm = str (GetPost(35.87139,128.5995743))
    print("##MDMonitor : Daegoo : " + _tm)
    insertData(12,_tm)
    time.sleep(1)

    # 13 부산
    _tm = str (GetPost(35.1795546,129.0734528))
    print("##MDMonitor : Busan : " + _tm)
    insertData(13,_tm)
    time.sleep(1)

    # 14 제주도
    _tm = str (GetPost(33.5038303,126.4599603))
    print("##MDMonitor : Jaejoodo : " + _tm)
    insertData(14,_tm)
    time.sleep(1)
 


def GetPost(let,lon):
    
    
    header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    url = "http://apis.skplanetx.com/weather/dust?lon=" + str(lon) + "&lat=" + str(let) + "&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()
    # print (r2)
    print (r2["weather"]["dust"][0]["pm10"]["value"])

    return r2["weather"]["dust"][0]["pm10"]["value"]


def insertData(no,value):
    
    print ("[" + str(time.strftime('%Y-%m-%d %H:%M:%S')) +"] : " + "insert data...  ")
    _host = 'ja-cdbr-azure-west-a.cloudapp.net'
    _user = 'b777abef975cef'
    _pwd = '5ed53ece'
    _db = 'db-60a50c09-aa74'

    _time = time.strftime('%Y-%m-%d %H:%M:%S')

    db = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db,charset='utf8',autocommit=True)
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("""UPDATE soonsoonmd SET value=%s WHERE no=%s""", (value,no))

    db.commit()
    
    # disconnect from server
    db.close()
    print("inserted data")


def insertLog():

    print ("[" + str(time.strftime('%Y-%m-%d %H:%M:%S')) +"] : " + "log data...  ")
    _host = 'ja-cdbr-azure-west-a.cloudapp.net'
    _user = 'b777abef975cef'
    _pwd = '5ed53ece'
    _db = 'db-60a50c09-aa74'

    _time = time.strftime('%Y-%m-%d %H:%M:%S')

    db = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db,charset='utf8',autocommit=True)
    cursor = db.cursor()
    cursor.execute("""INSERT into soonsoonmd_log(time) values (%s)""", (_time))


    db.commit()


    # disconnect from server
    db.close()
    print("logged data")


#schedule.every(10).seconds.do(funcTimer)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# insertData(1,1.23)

end = False
def excute_fun (second):
    
    global end
    if end :
        return
    
    # print("aa")
    insertLog() #데이터를 기록한 시간을 남김
    funcTimer() #실제 데이터를 남김
    
    threading.Timer(second, excute_fun, [second]).start()

# excute_fun(60.0)
with daemon.DaemonContext():
    excute_fun(7185.0)
