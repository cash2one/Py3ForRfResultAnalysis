import datetime
from selenium import webdriver
import time
import os

def get_now_time():
    """获取当前时间"""
    # starttime = datetime.datetime.now().timetuple()
    starttime =time.mktime(datetime.datetime.now().timetuple())
    return starttime

def return_After_computing_time(lasttime,nowtime):
        """计算时间差，以秒为单位返回"""
        computingtime = (lasttime-nowtime)
        return computingtime

os.system('ipconfig')
a = get_now_time()
drvier =webdriver.Chrome()
drvier.get("https://hao.360.cn/")
time.sleep(10)
b = get_now_time()
print(b,a)
print(return_After_computing_time(b,a))