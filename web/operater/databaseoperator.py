import pymysql

class databaseoperator(object):

    def __init__(self,request):
        self.name = request.GET.get('name', '')
        self.IP_Address = request.GET.get('IP_Address', '')
        self.Port = int(request.GET.get('Port', ''))
        self.username = request.GET.get('username', '')
        self.password = request.GET.get('password', '')

    def conn(self):
        try:
            conn = pymysql.connect(host = self.IP_Address, port = self.Port, user = self.username, passwd = self.password, db = self.name )

            cursor = conn.cursor()
            return cursor
        except Exception as e:
            print("Can't connect to MySQL server on %s"%self.name)


