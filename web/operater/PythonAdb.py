import os
import configparser
import monkey
import common


class PythonAdb(object):

    def __init__(self,a):
        # print(a)
        # cm = request.GET.get('name', '')
        self.mk = monkey.Monkey()
        self.cm = common.Common()
        self.cf = configparser.ConfigParser()
        # self.L = []

        self.b = a
        print(type(self.b))
        # self.L.append(request.GET.get('p', ''))
        # self.L.append(request.GET.get('r', ''))
        # self.L.append(request.GET.get('t', ''))
        # self.L.append(request.GET.get('m', ''))
        #
        # print(' '.join(self.L))
        # self.b = ' '.join(self.L)

    def get_devices(self):
        self.a = os.popen('adb devices')
        self.devices = self.a.readlines()
        self.dev = self.devices[1].split('\t')[0]

        return self.dev

    def adb_operator(self):
        pa = '222'
        print(pa)
        self.a = os.popen('adb shell monkey '+self.b)

        # return self.a

        # spl = devices[1]