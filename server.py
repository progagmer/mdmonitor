import threading
import datetime
import requests, json

def funcTimer():

    
    # 10 초마다 새로 고침.

    # 1 서울 데이터.
    timer = threading.Timer(10, funcTimer)
    timer.start()
    _tm = str (GetPost(37.5714,126.9658));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Seoul : " + _tm)

    # 2 경기 북부 데이터.
    _tm = str (GetPost(37.7491363,127.0532272));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungGiDoNorth : " + _tm)

    # 3 경기 남부 데이터, 수원시
    _tm = str (GetPost(37.2430863,127.0089135));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungGiSuwon : " + _tm)
    
    # 4 강원도 속초 시청
    _tm = str (GetPost(38.2046487,128.5710904));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : GanwondoSokCho : " + _tm)
    
    # 5 강원도 삼척 시청
    _tm = str (GetPost(37.4435487,129.1467404));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : GangwonSamcheok : " + _tm)
    
    # 6 충북
    _tm = str (GetPost(36.6354049,127.489273));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Chungbook : " + _tm)
    
    # 7 충남
    _tm = str (GetPost(36.9405641,126.4842582));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : ChungNam : " + _tm)

    # 8 전북
    _tm = str (GetPost(35.7223842,125.8176828));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : JeonBook : " + _tm)

    # 8 전남
    _tm = str (GetPost(34.8144255,126.4595968));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : JeonNam : " + _tm)

    # 9 광주시
    _tm = str (GetPost(36.3397103,125.9322271));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : GwankJoo : " + _tm)

    # 10 경북
    _tm = str (GetPost(36.233161,128.2744885));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungBook : " + _tm)

    # 10 경남
    _tm = str (GetPost(35.2369865,128.6900537));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungNam : " + _tm)
    
    # 11 대구
    _tm = str (GetPost(35.87139,128.5995743));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Daegoo : " + _tm)

    # 11 부산
    _tm = str (GetPost(35.1795546,129.0734528));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Busan : " + _tm)

    # 12 인천
    _tm = str (GetPost(37.4668428,126.667171));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Incheon : " + _tm)

    # 13 대전
    _tm = str (GetPost(36.3341548,127.3904357));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Daecheon : " + _tm)

    # 14 제주도
    _tm = str (GetPost(33.5038303,126.4599603));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Jaejoodo : " + _tm)

    # 15 울릉도
    _tm = str (GetPost(37.5063677,130.8549649));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Ulengdo : " + _tm)


def GetPost( lon, let):

    header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    url = "http://apis.skplanetx.com/weather/dust?lon=" + str(lon) + "&lat=" + str(let) + "&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()
    #print (r2)
    print (r2["weather"]["dust"][0]["pm10"]["value"])

funcTimer()