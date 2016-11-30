__auth='吕梓清'

import requests


class operator(object):

    def __init__(self,url,files):
        self.url = url
        self.files = files

    def create_new(self):
        url = self.url
        # data = {
        #     'systemName': '内业系统', 'title': '123', 'format': 'jpg', 'belongID': '2', 'belongPID': '2', 'belongDesc': '2'
        #     # 'name':'232','IP_Address':'232','Port':908,'username':'333','password':'232'
        # }
        files = {'file': (open(self.files, 'rb'))}

        r = requests.post(url, files=files)
        print(r.status_code, r.headers['Content-Type'], r.encoding, r.text)
        if r.status_code!=200:
            return '失败'
        else:
            return '成功'

        # print(data)

    def delete_old(self):
        url = self.url
        print(url)
        r = requests.delete(url)
