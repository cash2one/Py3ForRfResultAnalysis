import os
import configparser
import common

class Monkey(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read('monkey.conf')
        self.cm = common.Common()

    def run(self,command):
        """
        控制shell执行命令
        :param command:命令的文本
        :return:None
        """
        os.system(command)

    def get_comand(self):
        data = ''