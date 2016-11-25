import os
import configparser
import monkey
import common


class PythonAdb(object):

    def __init__(self):
        self.mk = monkey.Monkey()
        self.cm = common.Common()
        self.cf = configparser.ConfigParser()

    def get_devices(self):
        a = os.popen('adb devices')
        devices = a.readlines()
        dev = devices[1].split('\t')[0]
        return dev


        # spl = devices[1]