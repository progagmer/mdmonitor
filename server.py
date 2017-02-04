import threading
import datetime

def funcTimer(count):

    print("Server recording.....")
    #현재시간 출력
    print(str(count)+" "+str(datetime.datetime.now()))
    count += 1
    #threading.Timer(delay, 함수, args=[매개변수,]) - delay초 후에 함수실행
    timer = threading.Timer(1, funcTimer, args=[count])
        #timer 시작
    timer.start()
        #timer.cancel()        #타이머 취소


funcTimer(0)