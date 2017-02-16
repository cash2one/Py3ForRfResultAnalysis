import os
import configparser
import monkey
import common


class PythonAdb(object):

    def __init__(self,L):
        # print(a)
        # cm = request.GET.get('name', '')
        self.mk = monkey.Monkey()
        self.cm = common.Common()
        self.cf = configparser.ConfigParser()
        self.L = L

        print(L)
        # self.L.append(request.GET.get('p', ''))
        # self.L.append(request.GET.get('r', ''))
        # self.L.append(request.GET.get('t', ''))
        # self.L.append(request.GET.get('m', ''))
        #
        # print(' '.join(self.L))
        # self.b = ' '.join(self.L)

    def get_devices(self):
        """
        获取驱动
        """
        self.a = os.popen('adb devices')
        self.devices = self.a.readlines()
        self.dev = self.devices[1].split('\t')[0]

        return self.dev

    def adb_con(self,ip):
        """
        获取连接
        """
        self.connnect = 'adb connect %s'%ip
        self.a = os.popen(self.connnect).read().split()
        return self.a

    def adb_operator(self):
        # self.m = self.b.append(0,'adb shell monkey')
        print('adb shell monkey '+self.L)
        self.a = os.popen('adb shell monkey '+self.L)

        return self.a



        # spl = devices[1]