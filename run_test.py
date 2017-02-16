import unittest
from HTMLTestRunner3 import HTMLTestRunner
import time
from selenium import webdriver
from email.mime.text import MIMEText
from email.header import Header
import smtplib,os
from web.models import *
from django.db.models import Q
import sys
import time
import platform
from web.operater.function import function
import re


sys.path.append('\common')
from web.common import location

class MyTestCase(unittest.TestCase):


    def __getattr__(self, name):
        print(name)
        totalid = re.sub("\D","",name)
        print(totalid)
        print(name[len(totalid):])
        # newname = name[len(totalid):]
        id = uicase.objects.filter(Q(casename=name))
        print(id)
        def newname():
            print(int(totalid))
            print('23423423')
            browser=caserun(int(totalid))

            # print(self.assertEqual(2, 2, "testError"))
            # browser = location.open('Chrome', 'http://www.baidu.com/')
            #
            # # self.browser.maximize_window()
            # time.sleep(5)
            # print(location.Get_Text(browser, 'name=tj_trnuomi'))
            # location.Input_Text(browser, "name=wd", 'selenium1')
            # time.sleep(5)
            # print(location.Get_Value(browser, "id=kw"))
            # location.findID(browser, 'su').click()

            # function().Generate_picture(browser,name)


            # self.browser.find_element_by_xpath('//*[@id="u_sp"]/a[1]').click()
            # self.assertEqual(test,'糯米',"testError")
            self.assertEqual(2, 3, "testError")
        return newname

y = 0
k = []
b = []
m = []

def caserun(aid):
        print(aid)
        # new = casestep.objects.filter(Q(itemID=aid))
        new = casestep.objects.filter(Q(itemID=aid))
        for n in new:
            if n.kword.lower() == 'Open'.lower():
                browser = location.open(n.Roadking, n.Param)
                function().Generate_picture(browser, n.kword)
                b.append(browser)
                # print(b[0])
            elif n.kword.lower() == 'Input_Text'.lower():
                location.Input_Text(browser, n.Roadking, n.Param)
                time.sleep(10)
            elif n.kword.lower() == 'New_Click'.lower():
                # print(b[0])
                if b[0] is not None:
                    location.New_Click(browser, n.Roadking)
                elif m[0] is not None:
                    print(k[0])
                    location.New_Click(k[0], n.Roadking)
                time.sleep(38)
            elif n.kword.lower() == 'new_browser_close'.lower():
                time.sleep(5)
                location.new_browser_close(browser)
            elif uicase.objects.filter(Q(casename=n.kword)).exists():
                # print(n.itemID)
                # lzq = uicase.objects.filter(id=n.itemID)
                # for ll in lzq:
                #     print(ll.itemID)
                browser = new2(aid, n.kword)
                function().Generate_picture(browser, n.kword)
                m.append(browser)



def new2(aid, new, m=None):
        print(aid, new)
        print('吕梓清')
        if uicase.objects.filter(Q(casename=new)).exists():
            lzq = uicase.objects.filter(id=aid)
            n = uicase.objects.filter(itemID=lzq.get(id=aid).itemID).get(casename=new)
            # n = uicase.objects.get(casename=new)
            # n = uicase.objects.get(casename=new)
            print(n.id, n.casename)
            new = casestep.objects.filter(Q(itemID=n.id))

            for n in new:
                print(n.kword)
                if n.kword.lower() == 'Open'.lower():
                    browser = location.open(n.Roadking, n.Param)
                    k.append(browser)


                elif n.kword.lower() == 'Input_Text'.lower():
                    print('黄远阜')
                    location.Input_Text(k[y - 1], n.Roadking, n.Param)
                    time.sleep(10)
                elif n.kword.lower() == 'New_Click'.lower():
                    print('黄')
                    browser = location.New_Click(k[y - 1], n.Roadking)
                    time.sleep(38)
                elif n.kword.lower() == 'new_browser_close'.lower():
                    location.new_browser_close(k[y - 1])
                print(k[0])

            return k[0]


            #
    # def testCase1(self):
    #     self.assertEqual(2,2,"testError")


    # def testCase2(self):
    #     self.assertEqual(2,3,"testError")
    #
    # def testCase3(self):
    #     self.assertEqual(2,2,"testError")

if __name__ == '__main__':
    # print(platform.system())
    test_app = "./web"  # 定义测试应用
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(test_app + "/report/" + now_time + "result.html", 'wb')
    runner = HTMLTestRunner(fp,
                            title="xxx测试报告",
                            description="运行环境：%s, %s"%(platform.system(),"Chrome"))
    # discover = unittest.defaultTestLoader.discover(test_app + "/test_case", pattern='*_case.py')
    suiteTest = unittest.TestSuite()
    # h=MyTestCase().__getattr__('testCase1')

    suiteTest.addTest(MyTestCase("登录"))

    # suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(MyTestCase("退出"))
    suiteTest.addTest(MyTestCase("注册"))
    # suiteTest.addTest(MyTestCase("testCase3"))
    runner.run(suiteTest)
    fp.close()
