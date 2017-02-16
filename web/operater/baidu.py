#coding=utf-8
from selenium import webdriver
import sys
import time

sys.path.append('\common')
from web.common import location



browser=location.open('Chrome','http://www.baidu.com/')
time.sleep(4)
# location.findLinkText(browser,'糯米').click()
# time.sleep(3)

print(location.Get_Text(browser,'name=tj_trnuomi'))
location.Input_Text(browser,"name=wd",'selenium1')
time.sleep(5)
print(location.Get_Value(browser,"id=kw"))
location.findID(browser,'su').click()

time.sleep(3)
# location.close(browser)
location.new_browser_close(browser)