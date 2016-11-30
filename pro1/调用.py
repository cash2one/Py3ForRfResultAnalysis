__auth = '吕梓清'
import http.cookiejar
import urllib.request

from pro1.图片水印 import img

cookie = http.cookiejar.CookieJar()
cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cjhdr)
from pro1.新增 import operator

for i in range (2):
    print(i)
    m,new = img('C:\\Users\\Administrator\\Desktop\\Chrysanthemum.jpg',i,'C:\\Users\\Administrator\\Desktop\\').img()
    n = new.split('\\')[-1]
    print(new,n)

    #新增
    url = "http://123.57.20.27:8082/ResourcesPoolWrite/ExtAPI/extend/Create?title=测试图片&format=jpg&belongPID=2&belongDesc=2&systemName=内业系统&belongID=2"
    url1 = "http://123.57.20.27:8082/ResourcesPoolWrite/ExtAPI/extend/Create?title=测试图片&format=jpg&belongPID=2&belongDesc=2&systemName=内业系统&belongID=2"
    url2 = 'C:\\Users\\Administrator\\Desktop\\0.jpg'
    # data = {
    #     'systemName': '内业系统','title':'123', 'format': 'jpg', 'belongID': '2', 'belongPID': '2', 'belongDesc': '2'
    #     # 'name':'232','IP_Address':'232','Port':908,'username':'333','password':'232'
    # }
    # files = {'file':(open(new, 'rb'))}
    #
    # r = requests.post(url,files=files)
    # print(r.status_code,r.headers['Content-Type'],r.encoding,r.text)
    #
    # print(data)
    operator(url,new).create_new()
    







