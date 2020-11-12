import time
from datetime import datetime
import requests
import win32api

def getTime():
    """
    url = 'https://a.jd.com//ajax/queryServerData.html'
    ret = requests.get(url).text
    js = json.loads(ret)
    """
    t0 = datetime.now()
    url = 'https://a.jd.com//ajax/queryServerData.html'
    js = requests.get(url).json()
    t1 = datetime.now()
    t = float(js["serverTime"]) / 1000
    dt = datetime.fromtimestamp(t) + ((t1 - t0) / 2)

    return dt

def setSystemTime():
    url = 'https://a.jd.com//ajax/queryServerData.html'
    session = requests.session()

    # get server time
    t0 = datetime.now()
    js = session.get(url).json()
    t1 = datetime.now()
    t = float(js["serverTime"]) / 1000
    dt = datetime.fromtimestamp(t) + ((t1 - t0) / 2)
    tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(
        time.mktime(dt.timetuple()))
    msec = dt.microsecond / 1000
    win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, int(msec))

if __name__ == '__main__':
    setSystemTime()
    #运行一次后，在本条语句前加#注释后可以查看时间同步情况
    print("京东时间:%s\n本地时间:%s"%(getTime(),datetime.now()))