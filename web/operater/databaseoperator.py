import pymysql

class databaseoperator(object):

    def __init__(self,request,name,IP_Address,Port,username,password):
        # self.name = request.GET.get('name', '')
        # self.IP_Address = request.GET.get('IP_Address', '')
        # self.Port = request.GET.get('Port', '')
        # self.username = request.GET.get('username', '')
        # self.password = request.GET.get('password', '')
        self.name = name
        self.IP_Address = IP_Address
        self.Port = Port
        self.username = username
        self.password = password
        request.session['name'] = self.name
        request.session['IP_Address'] = self.IP_Address
        request.session['Port'] = self.Port
        request.session['username'] = self.username
        request.session['password'] = self.password

    def conn(self):
        # try:
            if not self.name:
                raise(NameError,'没有设置数据库信息')
            # try:
            elif self.username != ''and self.Port!='' and self.username!='':
                  self.conn = pymysql.connect(host = self.IP_Address, port = int(self.Port), user = self.username, passwd = self.password, db = self.name )
                  cursor = self.conn.cursor()
                  if not cursor:
                      raise (NameError, "连接数据库失败")
                  else:
                      return cursor
            else:
                    print('账号或端口或用户名称不能为空')


        # except Exception as e:
        #     print("Can't connect to MySQL server on %s"%self.name)

    def spiltdatabase(self,parameter):
        cur = self.conn()
        self.data = parameter.split(' ')
        if self.data[1]=='*':
            cur.execute("SHOW columns from "+self.data[-1])
            reList = cur.fetchall()
            return reList
        else:
            self.data1 = self.data[1].split(',')
            print(self.data1)
            return self.data1

    def ExecQuery(self,parameter):
        cur = self.conn()
        cur.execute(parameter)
        # data = self.spiltdatabase(parameter)
        reList = cur.fetchall()

        self.conn.close()
        return reList

        # row_1 = self.conn().fetchone()
        # return row_1

    def updateData(self,parameter):
        try:

            cur = self.conn()
            cur.execute(parameter)
            self.conn.commit()
        except Exception  as e:
            print(e)

    # def insertData(self,parameter):
    #     cur = self.conn()
    #     cur.execute(parameter)
    #     self.conn.commit()





