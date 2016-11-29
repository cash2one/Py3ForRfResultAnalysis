__auth = '吕梓清'
"""
检测资源资源：内存、CPU、网络、流量、电量等
"""
import subprocess
class PyPerforman(object):
    def __init__(self,pkg_name):
        self.pkg_name = pkg_name
        self.cpu = []
        self.men = []

    #获取CPU
    def Per_cpu(self):
        # cmd1 = 'dumpsys cpuinfo |grep '+self.pkg_name
        # cmd1 = 'top |grep '+self.pkg_name
        cmd1 = 'top -n %s -d %s -s cpu | grep %s$' %(str(10),str(2), self.pkg_name)
        cmd2 = 'adb shell '
        cmd = cmd2 +"\""+cmd1+"\""
        print(cmd)
        temp = []
        top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        print(top_info)
        for info in top_info:
            temp.append(info.split()[2].decode())  # bytes转换为string
            print("cpu占用:%s" %temp)
        for i in temp:
            if i != "0%":
                self.cpu.append(i.split("%")[0])
        print(self.cpu)
        return self.cpu

    #获取内存信息
    def Per_men(self):
        # cmd1 = "dumpsys  meminfo %s"  %(self.pkg_name)
        cmd = "adb shell dumpsys  meminfo %s"%(self.pkg_name)
        print(cmd)
        temp = []
        top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        print(top_info)
        for info in top_info:
            temp.append(info.split())
            print(temp)
            # print("内存占用:%s" %temp[10][0].decode()+"K")
        temp.append(temp)
        for t in temp:
            # self.men.append(t[19][1].decode())
            print(t)
        return self.men