import threading
import datetime
import requests, json

def funcTimer(count):

    print("Timer Expired")
    #현재시간 출력
    print(str(count)+" "+str(datetime.datetime.now()))

    count += 1
    #threading.Timer(delay, 함수, args=[매개변수,]) - delay초 후에 함수실행
    timer = threading.Timer(5, funcTimer, args=[count])
    GetPost()
    GetPost()
        #timer 시작
    timer.start()
        #timer.cancel()        #타이머 취소

def GetPost():

    header = {'appKey': '153c3607-dc80-352b-9568-478315f12286'}
    url = "http://apis.skplanetx.com/weather/dust?lon=126.9658000000&lat=37.5714000000&version=1"
    r = requests.get(url , headers = header)
    r2 = r.json()

    print (r2["weather"]["dust"][0]["pm10"]["value"])

funcTimer(0)