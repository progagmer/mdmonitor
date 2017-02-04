import threading
import datetime
import requests, json

def funcTimer():

    
    # 10 초마다 새로 고침.

    # 서울 데이터.
    timer = threading.Timer(10, funcTimer)
    timer.start()
    _tm = str (GetPost(37.5714,126.9658));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Seoul : " + _tm)

    #경기 북부 데이터.
    _tm = str (GetPost(37.7491363,127.0532272));
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungGiDoNorth : " + _tm)
    


def GetPost( lon, let):

    header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    url = "http://apis.skplanetx.com/weather/dust?lon=" + lon + "lat=" + let + "&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()

    print (r2["weather"]["dust"][0]["pm10"]["value"])

funcTimer()