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

_nowTime = int(dt.datetime.now().hour)
print(_nowTime)