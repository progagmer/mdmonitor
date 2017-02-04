import threading
import datetime
import requests, json
import time

def funcTimer(count):

    # 10 초마다 새로 고침.

    # 1 서울 데이터.
    count += 1
    timer = threading.Timer(60, funcTimer)
    timer.start()
    print (str(count) + "회차")
    _tm = str (GetPost(37.5714,126.9658));
    print("##MDMonitor : Seoul : " + _tm)
    time.sleep(1)

    # 3 경기 남부 데이터, 수원시
    _tm = str (GetPost(37.2430863,127.0089135));
    print("##MDMonitor : KyungGiSuwon : " + _tm)
    time.sleep(1)
    
    # 4 강원도 속초 시청
    _tm = str (GetPost(38.2046487,128.5710904));
    print("##MDMonitor : GanwondoSokCho : " + _tm)
    time.sleep(1)
    
    # 5 강원도 삼척 시청
    _tm = str (GetPost(37.4435487,129.1467404));
    print("##MDMonitor : GangwonSamcheok : " + _tm)
    time.sleep(1)
    
    # 6 충북
    _tm = str (GetPost(36.6354049,127.489273));
    print("##MDMonitor : Chungbook : " + _tm)
    time.sleep(1)
    

    # 8 전북
    _tm = str (GetPost(35.7223842,125.8176828));
    print("##MDMonitor : JeonBook : " + _tm)
    time.sleep(1)
    # 8 전남
    _tm = str (GetPost(34.8144255,126.4595968));
    print("##MDMonitor : JeonNam : " + _tm)
    time.sleep(1)
    # 9 광주시
    _tm = str (GetPost(36.3397103,125.9322271));
    print("##MDMonitor : GwankJoo : " + _tm)
    time.sleep(1)
    # 10 경북
    _tm = str (GetPost(36.233161,128.2744885));
    print("##MDMonitor : KyungBook : " + _tm)
    time.sleep(1)

    # 11 대구
    _tm = str (GetPost(35.87139,128.5995743));
    print("##MDMonitor : Daegoo : " + _tm)
    time.sleep(1)

    # 11 부산
    _tm = str (GetPost(35.1795546,129.0734528));
    print("##MDMonitor : Busan : " + _tm)
    time.sleep(1)

    # 12 인천
    _tm = str (GetPost(37.4668428,126.667171));
    print("##MDMonitor : Incheon : " + _tm)
    time.sleep(1)

    # 13 대전
    _tm = str (GetPost(36.3341548,127.3904357));
    print("##MDMonitor : Daecheon : " + _tm)
    time.sleep(1)

    # 14 제주도
    _tm = str (GetPost(33.5038303,126.4599603));
    print("##MDMonitor : Jaejoodo : " + _tm)
    time.sleep(1)

    # 15 울릉도
    _tm = str (GetPost(37.5063677,130.8549649));
    print("##MDMonitor : Ulengdo : " + _tm)
    time.sleep(1)


def GetPost(let,lon):

    header = {'appKey': '51db30bf-0f11-3b17-92fe-4ee662af9ef8'}
    url = "http://apis.skplanetx.com/weather/dust?lon=" + str(lon) + "&lat=" + str(let) + "&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()
    #print (r2)
    #print (r2["weather"]["dust"][0]["pm10"]["value"])

    return r2["weather"]["dust"][0]["pm10"]["value"]

funcTimer(0)