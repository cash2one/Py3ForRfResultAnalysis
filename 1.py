import datetime
from selenium import webdriver
import time
import os
import run_test

def get_now_time():
    """获取当前时间"""
    # starttime = datetime.datetime.now().timetuple()
    starttime =time.mktime(datetime.datetime.now().timetuple())
    return starttime

def return_After_computing_time(lasttime,nowtime):
        """计算时间差，以秒为单位返回"""
        computingtime = (lasttime-nowtime)
        return computingtime
class new(object):
    def 登录(self):
        self.m = '登录'
        print(self.m)

os.system('ipconfig')
a = get_now_time()
drvier =webdriver.Chrome()
drvier.get("https://hao.360.cn/")
time.sleep(10)
b = get_now_time()
print(b,a)
print(return_After_computing_time(b,a))
new().登录()




#coding=utf-8
# from selenium import webdriver
# from time import sleep
# import unittest
#
# class baiduTest(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         sleep(10)
#         self.base_url = "http://www.baidu.com"
#
#     def test_case(self):
#         driver = self.driver
#         driver.get(self.base_url)
#         driver.click_text("设置")
#         driver.click_text("搜索设置")
#         sleep(2)
#         driver.click("//a[@class='prefpanelgo']")
#         sleep(1)
#         driver.accept_alert()
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     TestRunner(r".\demo").run()