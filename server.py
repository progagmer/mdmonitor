import threading
import datetime
import requests, json
import time
import schedule

import urllib
import pymysql
from urllib.request import urlopen

# from daemon import runner


# class App():

#     def __init__(self):
#         self.stdin_path = '/dev/null'
#         self.stdout_path = '/dev/tty'
#         self.stderr_path = '/dev/tty'
#         self.pidfile_path =  '/tmp/foo.pid'
#         self.pidfile_timeout = 5

#     def run(self):

#         while True:
#             print("Howdy!  Gig'em!  Whoop!")
#             time.sleep(10)




   

    # def funcTimer():

    #     # 10 cho.
    #     insertData()
    #     # 1 서울 데이터.
    #     _tm = str (GetPost(37.5714,126.9658))
    #     print("##MDMonitor : Seoul : " + _tm)
    #     time.sleep(1)

    #     # 3 경기 남부 데이터, 수원시
    #     _tm = str (GetPost(37.2430863,127.0089135))
    #     print("##MDMonitor : KyungGiSuwon : " + _tm)
    #     time.sleep(1)
        
    #     # 4 강원도 속초 시청
    #     _tm = str (GetPost(38.2046487,128.5710904))
    #     print("##MDMonitor : GanwondoSokCho : " + _tm)
    #     time.sleep(1)
        
    #     # 5 강원도 삼척 시청
    #     _tm = str (GetPost(37.4435487,129.1467404))
    #     print("##MDMonitor : GangwonSamcheok : " + _tm)
    #     time.sleep(1)
        
    #     # 6 충북
    #     _tm = str (GetPost(36.6354049,127.489273))
    #     print("##MDMonitor : Chungbook : " + _tm)
    #     time.sleep(1)
        

    #     # 8 전북
    #     _tm = str (GetPost(35.7223842,125.8176828))
    #     print("##MDMonitor : JeonBook : " + _tm)
    #     time.sleep(1)
    #     # 8 전
    #     _tm = str (GetPost(34.8144255,126.4595968))
    #     print("##MDMonitor : JeonNam : " + _tm)
    #     time.sleep(1)
    #     # 9 광주시
    #     _tm = str (GetPost(36.3397103,125.9322271))
    #     print("##MDMonitor : GwankJoo : " + _tm)
    #     time.sleep(1)
    #     # 10 경북
    #     _tm = str (GetPost(36.233161,128.2744885))
    #     print("##MDMonitor : KyungBook : " + _tm)
    #     time.sleep(1)

    #     # 11 대구
    #     _tm = str (GetPost(35.87139,128.5995743))
    #     print("##MDMonitor : Daegoo : " + _tm)
    #     time.sleep(1)

    #     # 11 부산
    #     _tm = str (GetPost(35.1795546,129.0734528))
    #     print("##MDMonitor : Busan : " + _tm)
    #     time.sleep(1)

    #     # 12 인천
    #     _tm = str (GetPost(37.4668428,126.667171))
    #     print("##MDMonitor : Incheon : " + _tm)
    #     time.sleep(1)

    #     # 13 대전
    #     _tm = str (GetPost(36.3341548,127.3904357))
    #     print("##MDMonitor : Daecheon : " + _tm)
    #     time.sleep(1)

    #     # 14 제주도
    #     _tm = str (GetPost(33.5038303,126.4599603))
    #     print("##MDMonitor : Jaejoodo : " + _tm)
    #     time.sleep(1)

    #     # 15 울릉도
    #     _tm = str (GetPost(37.5063677,130.8549649))
    #     print("##MDMonitor : Ulengdo : " + _tm)
    #     time.sleep(1)


    # def GetPost(let,lon):
        
    #     print("test....")
        
    #     # header = {'appKey': '51db30bf-0f11-3b17-92fe-4ee662af9ef8'}
    #     # url = "http://apis.skplanetx.com/weather/dust?lon=" + str(lon) + "&lat=" + str(let) + "&version=1"
    #     # r = requests.get(url , headers = header)
    #     # r2 = r.json()
    #     # print (r2)
    #     # #print (r2["weather"]["dust"][0]["pm10"]["value"])

    #     # return r2["weather"]["dust"][0]["pm10"]["value"]

    #     #schedule.every(10).seconds.do(funcTimer)

    

   

    

def insertData():

    print ("[" + str(time.strftime('%Y-%m-%d %H:%M:%S')) +"] : " + "log data...  ")
    _host = 'ja-cdbr-azure-west-a.cloudapp.net'
    _user = 'b777abef975cef'
    _pwd = '5ed53ece'
    _db = 'db-60a50c09-aa74'

    _time = time.strftime('%Y-%m-%d %H:%M:%S')

    db = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db,charset='utf8',autocommit=True)
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("""INSERT into datarecord (time,s1,s2) values (%s,%s, %s)""", ("TestForServer", 1, 2))

    db.commit()
    
    # disconnect from server
    db.close()
    
#     insertData

end = False
def excute_fun(second):
    
    global end
    if end :
        return
    
    # print("aa")
    insertData()
    threading.Timer(second, excute_fun, [second]).start()


excute_fun(10)

# while True:
#         schedule.run_pending()
#         time.sleep(5)
#         insertData()

# app = App()
# daemon_runner = runner.DaemonRunner(app)
# daemon_runner.do_action()





