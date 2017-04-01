import threading
import datetime
import requests, json
import time
import datetime as dt
import schedule

import urllib
import pymysql
from urllib.request import urlopen
from pyfcm import FCMNotification
import daemon
    
#get sever now value
_nowDataDic =[]

def GetSeverData():
    
    _host = 'ja-cdbr-azure-west-a.cloudapp.net'
    _user = 'b777abef975cef'
    _pwd = '5ed53ece'
    _db = 'db-60a50c09-aa74'

    _time = time.strftime('%Y-%m-%d %H:%M:%S')

    db = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db,charset='utf8',autocommit=True)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute("""
                SELECT *
                FROM soonsoonmd
                """)

    result = cursor.fetchall()
    for value in result:
        _nowDataDic.append(float(value[2]))

    db.commit()
    db.close()
    

#지금 현재값을 받아와서 다른지 체크해준다.
def GetNowChange( _nowValue,num ):
    resultValue = False
    nowNum = 0
    pastNum = 0
    nowValueF = float(_nowValue)
    pastValueF = float(_nowDataDic[num])

    #현재 받아온 값이 어떤 등급인지 계산
    if( nowValueF < 30):
        nowNum = 0
    elif(nowValueF < 50):
        nowNum = 1
    elif(nowValueF < 100):
        nowNum = 2    
    else:
        nowNum = 3        

    #현재 받아온 값이 어떤 등급인지 계산
    if( pastValueF < 30):
        pastNum = 0
    elif(pastValueF < 50):
        pastNum = 1
    elif(pastValueF < 100):
        pastNum = 2    
    else:
        pastNum = 3     

    if( nowNum != pastNum):
        #저장되었던 등급과 지금의 등급이 변경되었으므로 알림을 해줌.
        resultValue = True

    print(resultValue)
    return resultValue


def funcTimer():

    #현재 서버 데이터를 가져온다.
    GetSeverData()

    # 1 서울 데이터.
    _tm = str (GetPost(37.5714,126.9658))
    print("##MDMonitor : Seoul : " + _tm)
    insertData(1,_tm)
    # if(GetNowChange(_tm,0)):
    _localeName = "서울과 경기북동부"
    DustCall("Seoul",_tm) #FCM 으로 콜.    
    time.sleep(10)

    # 2 인천
    _tm = str (GetPost(37.4561057,126.7052611))
    print("##MDMonitor : Incheon : " + _tm)
    insertData(2,_tm)
    # if(GetNowChange(_tm,1)):
    _localeName = "인천,경기서부"
    DustCall("Incheon",_tm) #FCM 으로 콜.
    time.sleep(10)

    # 3 경기 남부 데이터, 수원시
    _tm = str (GetPost(37.2430863,127.0089135))
    print("##MDMonitor : KyungGiSuwon : " + _tm)
    # if(GetNowChange(_tm,2)):
    _localeName = "수원,경기남부"
    DustCall("KyungGiSuwon",_tm) #FCM 으로 콜.
    insertData(3,_tm)
    time.sleep(10)
    
    # 4 강원도 속초 시청
    _tm = str (GetPost(38.2046487,128.5710904))
    print("##MDMonitor : GanwondoSokCho : " + _tm)
    # if(GetNowChange(_tm,3)):
    _localeName = "속초,강원도북부"
    DustCall("GanwondoSokCho",_tm) #FCM 으로 콜.
    insertData(4,_tm)
    time.sleep(10)
    
    # 5 강원도 삼척 시청
    _tm = str (GetPost(37.4435487,129.1467404))
    print("##MDMonitor : GangwonSamcheok : " + _tm)
    # if(GetNowChange(_tm,4)):
    _localeName = "삼척,강원도남부"
    DustCall("GangwonSamcheok",_tm) #FCM 으로 콜.
    insertData(5,_tm)
    time.sleep(10)
    
    # 6 충북
    _tm = str (GetPost(36.6354049,127.489273))
    print("##MDMonitor : Chungbook : " + _tm)
    # if(GetNowChange(_tm,5)):
    _localeName = "천안,충북"
    DustCall("Chungbook",_tm) #FCM 으로 콜.
    insertData(6,_tm)
    time.sleep(10)

    # 7 대전
    _tm = str (GetPost(36.350412,127.384547))
    print("##MDMonitor : Daecheon : " + _tm)
    # if(GetNowChange(_tm,6)):
    _localeName = "대전,충남"
    DustCall("Daecheon",_tm) #FCM 으로 콜.
    insertData(7,_tm)
    time.sleep(10)
    
    # 8 전북
    _tm = str (GetPost(35.7223842,125.8176828))
    print("##MDMonitor : JeonBook : " + _tm)
    # if(GetNowChange(_tm,7)):
    _localeName = "전주,전북"
    DustCall("JeonBook",_tm) #FCM 으로 콜.
    insertData(8,_tm)
    time.sleep(10)

    # 9 전남
    _tm = str (GetPost(34.8144255,126.4595968))
    print("##MDMonitor : JeonNam : " + _tm)
    # if(GetNowChange(_tm,8)):
    _localeName = "목포,전남"
    DustCall("JeonNam",_tm) #FCM 으로 콜.
    insertData(9,_tm)
    time.sleep(10)

    # 10 광주시
    _tm = str (GetPost(35.1600765,126.851297))
    print("##MDMonitor : GwankJoo : " + _tm)
    # if(GetNowChange(_tm,9)):
    _localeName = "광주,전남중부"
    DustCall("GwankJoo",_tm) #FCM 으로 콜.
    insertData(10,_tm)
    time.sleep(10)

    # 11 경북
    _tm = str (GetPost(36.576111,128.5057068))
    print("##MDMonitor : KyungBook : " + _tm)
    # if(GetNowChange(_tm,10)):
    _localeName = "안동,경북"
    DustCall("KyungBook",_tm) #FCM 으로 콜.
    insertData(11,_tm)
    time.sleep(10)

    # 12 대구
    _tm = str (GetPost(35.87139,128.5995743))
    print("##MDMonitor : Daegoo : " + _tm)
    # if(GetNowChange(_tm,11)):
    _localeName = "대구,경남북부"
    DustCall("Daegoo",_tm) #FCM 으로 콜.
    insertData(12,_tm)
    time.sleep(10)

    # 13 부산
    _tm = str (GetPost(35.1795546,129.0734528))
    print("##MDMonitor : Busan : " + _tm)
    # if(GetNowChange(_tm,12)):
    _localeName = "부산,경남남부"
    DustCall("Busan",_tm) #FCM 으로 콜.
    insertData(13,_tm)
    time.sleep(10)

    # 14 제주도
    _tm = str (GetPost(33.5038303,126.4599603))
    print("##MDMonitor : Jaejoodo : " + _tm)
    # if(GetNowChange(_tm,13)):
    _localeName = "제주도"
    DustCall("Jaejoodo",_tm) #FCM 으로 콜.
    insertData(14,_tm)
    time.sleep(10)
 


def GetPost(let,lon):    
    _nowTime = int(dt.datetime.now().hour)
    if( (_nowTime < 12)):
        header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    else :
        header = {'appKey': '51db30bf-0f11-3b17-92fe-4ee662af9ef8'}
    
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


#
# FCM 에 연동하는 부분.


api_key = "AAAA3BAXVsw:APA91bHLptlteWrA-bRxxNCg-1ULXijihFl_R8Nu4-5ERBfF8GwcdkFuEiI_iCd3OI-wpZSnEgp6_D5hkSr4EZZ8b_Wj1MoAHvDe9DkvhVc0ih9S6ldGRa1TjD5xfm0DRIPDCegENTqy-3jcPbwct2Ww9oTr22MVPQ"


_localeName =""

def TitleSet(x):
    return {
        1: _localeName + " 지역 미세먼지 상태 좋음!", #적음
        2: _localeName + " 지역 미세먼지 보통, 주의", #보통
        3: _localeName + " 지역 미세먼지 나쁨, 마스크필수!", #많음
        4: _localeName + " 지역 미세먼지 매우나쁨, 외출금지!!", #매우많음
    }.get(x, "미세먼지를 확인해보세요.") #default

def MsgSet(x):
   return {
        1: "- 미세먼지가 적네요. 나들이도 괜찮습니다.", #적음
        2: "- 약간의 미세먼지가 있네요. 외출시 마스크 필수!!", #보통
        3: "- 미세먼지가 많아요! 외출 주의!! ", #많음
        4: "- 미세먼지가 매우 많습니다!! 오늘은 외출금지!", #매우많음
    }.get(x, "- 굽신 게임내에서 미세먼지를 연동하면 게임내 벌금이 감소됩니다.") #default
    

def SortDust(location,amount):
    #받아온 미세먼지 값을 이용하여, 현재 등급을 나눠준다.
    num_now = float(amount)
    if(num_now < 30): #미세먼지 매우 적음
        PostFCM (location,1)
    elif (num_now < 80): #미세먼지 적음
        PostFCM (location,2)
    elif (num_now < 150): #미세먼지 나쁨
        PostFCM (location,3)
    else: #미세먼지 매우나쁨
        PostFCM (location,4)

def DustCall(location,amount):
    _nowTime = int(dt.datetime.now().hour)
    print(_nowTime)

    if( (_nowTime < 13) and (_nowTime > 0) ):
        #오전 8시 이후, 오후 10시 이하.
        SortDust(location,amount)

def PostFCM(location,num):
    push_service = FCMNotification(api_key=api_key)
    message_title = TitleSet(num)
    message_body = MsgSet(num)
    result=push_service.notify_topic_subscribers(topic_name=location,message_title=message_title, message_body=message_body)


end = False
def excute_fun (second):
    
    global end
    if end :
        return
    insertLog() #데이터를 기록한 시간을 남김
    funcTimer() #실제 데이터를 남김
    
    threading.Timer(second, excute_fun, [second]).start()

with daemon.DaemonContext():
    excute_fun(3600.0)
