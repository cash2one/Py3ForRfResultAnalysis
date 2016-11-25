import configparser

class Common(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read('monkey.conf')
        self.all_list = ['package_name','apk_path']
