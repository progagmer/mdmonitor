import threading
import datetime
import requests, json

def funcTimer():

    
    # 10 초마다 새로 고침.
    timer = threading.Timer(5, funcTimer)
    timer.start()
    _tm = str (GetPost());
    print(str(datetime.datetime.now()))
    print("##MDMonitor : Seoul : " + _tm)

    timer = threading.Timer(1, funcTimer)
    timer.start()
    _tm = str (GetPost());
    print(str(datetime.datetime.now()))
    print("##MDMonitor : KyungGiDo : " + _tm)
    


def GetPost():

    header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    url = "http://apis.skplanetx.com/weather/dust?lon=126.9658000000&lat=37.5714000000&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()

    print (r2["weather"]["dust"][0]["pm10"]["value"])

funcTimer()