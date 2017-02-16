import datetime
import random
import pymysql
from django.http import JsonResponse

import django
import matplotlib.pyplot as plt
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure

from web.models import *
from web.models import result_test_runss
from django.db.models import Q
from web.operater.databaseoperator import databaseoperator
from web.operater.PythonAdb import PythonAdb
from web.operater.PythonPerformance import PyPerforman
import requests
import urllib

from selenium import webdriver

import sys
import time,platform

sys.path.append('\common')
from .common import location
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner3 import HTMLTestRunner
import unittest
from run_test import MyTestCase


# Create your views here.

#登录
def login_action(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        #寻找名称为'username'和'password'的POST 参数，而且如果参数没有提交，则返回一个空字符串
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print(username,password)
        if username == '' or password == '':
            return render(request,'Login.html',{'error':'账号或密码为空'})
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/index/')
            request.session['username'] = username
            return response

        else:
            return render(request,'Login.html',{'error':'用户名或密码错误'})



#首页
def index(request):
    result_list = result_test_runss.objects.all()
    username = request.session.get('username', '')

    paginator = Paginator(result_list, 10)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request,'Index.html',{"user":username,"events":contacts})

#退出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

#搜索
def sreach_name(request):
    username = request.session.get('username', '')
    sreach_name = request.GET.get("name", "")
    # sreach_casesname = request.GET.get("casesname", "")
    sreach_name_bytes = sreach_name.encode(encoding="utf-8")
    # sreach_casesname_bytes = sreach_casesname.encode(encoding="utf-8")

    print(sreach_name_bytes)
    # event_list = result_test_runss.objects.filter(source_file__contains=sreach_name_bytes).filter(id__contains = sreach_casesname)
    event_list = result_test_runss.objects.filter(Q(source_file__contains=sreach_name_bytes)|Q(id__contains = sreach_name_bytes)|Q(started_at__startswith=sreach_name))
    # started_at__contains = sreach_casesname.encode(encoding="utf-8")
    return render(request, "Index.html", {"user": username, "events": event_list})

#删除
def del_data(request,aid):
    # print('article_id %s' % aid)
    result_data = result_test_runss.objects.get(id = aid)
    result_data.delete()
    return HttpResponseRedirect('/index/')

def rep_del_data(request,aid):
    result_data = result_test_runss.objects.get(id = aid)
    result_data.delete()
    return HttpResponseRedirect('/report_list/')

#新增


#图标分析
def columnar_analysic(request):

    result_data = result_test_runss.objects.all()

    return render(request,'columnar_analysic.html',{'result_data':result_data})


def report_graph_analysis(request):
    result_data = result_test_runss.objects.all()
    return render(request,'report_graph_analysis.html',{"result_data":result_data})



#图标分析搜索
def sreach_name_result(request):
    username = request.session.get('username', '')
    sreach_name = request.GET.get("name", "")
    # sreach_casesname = request.GET.get("casesname","")

    sreach_name_bytes = sreach_name.encode(encoding="utf-8")
    # sreach_casesname_bytes = sreach_casesname.encode(encoding="utf-8")
    # print(sreach_name,sreach_casesname)
    # result_data = result_test_runss.objects.filter(source_file__contains=sreach_name_bytes).filter(id__contains = sreach_casesname)
    # result_data = result_test_runss.objects.filter( Q(finished_at__lte=sreach_casesname)and Q(started_at__gte=sreach_name) )
    result_data = result_test_runss.objects.filter(Q(source_file__contains=sreach_name_bytes) | Q(id__contains=sreach_name_bytes) | Q(started_at__startswith=sreach_name))


    # result_data = result_test_runss.objects.filter(Q(source_file__contains=sreach_name_bytes)|Q(started_at__gte=sreach_name))


    # print(result_data,)
    # if isinstance(result_data):
    #     result_data = result_data
    # else:
    #     result_data = result_test_runss.objects.filter(started_at__day=sreach_name_bytes)
    # result_data1 = result_test_runss.objects.filter(started_at__day=sreach_name_bytes)
    print(result_data)
    return render(request, "columnar_analysic.html", {"user": username, 'result_data':result_data})

#数据库连接页面显示
def databascon(request):
    return render(request, 'database_connection.html')

#数据库连接
def databasconn(request):
    try:
        name = request.GET.get('name', '')
        IP_Address = request.GET.get('IP_Address', '')
        Port = request.GET.get('Port', '')
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        # connn =databaseoperator(request).conn()
        connn = databaseoperator(request,name,IP_Address,Port,username,password).conn()
        print(connn)
        if connn is None:
            return render(request, 'database_connection.html', {'row_1': '连接失败'})
        else:
            # connn.execute("select * from web_result_test_runss")
            # connn.execute("select * from student")
            # row_1 = connn.fetchone()
            return render(request, 'database_connection.html', {'row_1':'连接成功'})
    except Exception as e:
        print(e)
        return render(request, 'database_connection.html',{'row_1': e})

#数据表创建
def data_create(request):
    name = request.GET.get('name','')
    IP_Address = request.GET.get('IP_Address','')
    Port = request.GET.get('Port','')
    username = request.GET.get('username','')
    password = request.GET.get('password','')
    print(name,IP_Address,Port,username,password)
    event_list = create_data.objects.filter(Q(IP_Address__contains=IP_Address))
    if create_data.objects.filter(Q(IP_Address__contains=IP_Address)).exists() and create_data.objects.filter(Q(Port__contains=Port)).exists():
        row_1 = '该数据已存在，不允许重新创建'
    else:
        add = create_data(name=name, IP_Address=IP_Address, Port=Port, username=username, password=password)
        add.save()
        row_1 = '该数据创建成功'

    return render(request, 'database_connection.html', {'row_1': row_1})

#数据库操作
def data_operation(request):
    try:
        name = request.session.get('name','')
        IP_Address = request.session.get('IP_Address','')
        Port = request.session.get('Port','')
        username = request.session.get('username','')
        password = request.session.get('password','')

        # print(name)
        conditions = request.GET.get('conditions', '')
        if conditions !="":
            new_conditions = conditions.split(' ')

            #数据库操作
            if new_conditions[0] == 'update' or new_conditions[0] == 'delete' or new_conditions[0] == 'insert':
                titlecon = databaseoperator(request,name,IP_Address,Port,username,password).updateData(conditions)

            # elif new_conditions[0] == 'insert':
            #     titlecon = databaseoperator(request, name, IP_Address, Port, username, password).insertData(conditions)

            print(conditions)
            titlecon = databaseoperator(request,name,IP_Address,Port,username,password).spiltdatabase(conditions)
            print(type(titlecon))
            connn = databaseoperator(request,name,IP_Address,Port,username,password).ExecQuery(conditions)
            print(len(titlecon))
            # connn.execute('SHOW columns from '+par)
            if isinstance(titlecon,list):
                return render(request, 'database_operation.html',{'connn': connn, 'leng': len(titlecon), 'titlecon': titlecon,'data1':'1'})
            else:
                return render(request, 'database_operation.html',{'connn': connn,'leng':len(titlecon),'titlecon':titlecon,'data1':'*'})
        else:
            return render(request, 'database_operation.html',)
    except Exception as e:
        print(e)
        return render(request, 'database_operation.html', )
        # for events in event_list:
    #     print(IP_Address,events.IP_Address)
    #     if IP_Address == events.IP_Address and Port==events.Port:
    #         row_1='该数据已存在，不允许重新创建'
    #         print(row_1)
    #         # return render(request, 'database_connection.html', {'row_1': row_1})
    #     else:
    #         add = create_data(name=name,IP_Address=IP_Address,Port=Port,username=username,password=password)
    #         add.save()
    #         row_1 = '该数据创建成功'

def database_list(request):
    #新数据库列表
    titlecon = databaseoperator(request,'rfresultanalysis','localhost','3307','root','').spiltdatabase('select * from web_create_data')
    connn = databaseoperator(request,'rfresultanalysis','localhost','3307','root','').ExecQuery('select * from web_create_data')
    return render(request,'database_list.html',{'titlecon': titlecon,'connn':connn,'data1':'*'})

def create_interfacetest(request):

    return render(request,'create_interfacetest.html')

def new_interfacetest(request):
    # result = createinterfacetest.objects.all()
    caseID = request.GET.get('caseID')
    name = request.GET.get('name')
    method = request.GET.get('method')
    page_content = request.GET.get('page_content')
    url = request.GET.get('url')
    parameter = request.GET.get('parameter')
    print(caseID,name,method,page_content,url,parameter)
    createinterfacetest.objects.create(caseID=caseID,name=name,method=method,contentType=page_content,URL=url,param=parameter).save()
    return render(request,'create_interfacetest.html')

def new_interfacetest_id(request,aid):
    usercaseID = aid
    caseID = request.GET.get('caseID')
    name = request.GET.get('name')
    method = request.GET.get('method')
    page_content = request.GET.get('api_contentType')
    url = request.GET.get('URL')
    parameter = request.GET.get('param')
    # print(caseID,name,method,page_content,url,parameter)
    createinterfacetest.objects.create(caseID=caseID, name=name, method=method, contentType=page_content, URL=url,
                                       param=parameter,usercaseID=usercaseID).save()
    result = createinterfacetest.objects.all()
    return render(request, 'interface_test_case.html',{'result':result})

def new_interfacetest_new(request,aid):
    return render(request,'newcase.html',{'usercaseID':aid})



def interface_test_case(request):
    result = createinterfacetest.objects.all()
    # connn = databaseoperator(request, 'rfresultanalysis', 'localhost', '3307', 'root', '').ExecQuery(
    #     'select * from web_createinterfacetest')
    return render(request,'interface_test_case.html',{'result':result})

def newcaseaggregate(request):
    usercasename = request.GET.get('name')
    casedescribe = request.GET.get('descript')
    print(usercasename,casedescribe)
    Use_case_management.objects.create(usercasename=usercasename,casedescribe=casedescribe).save()
    result = Use_case_management.objects.all()
    return render(request,'usecasemanagement.html',{'result':result})

def usecasemanagement(request):
    result = Use_case_management.objects.all()
    return render(request,'usecasemanagement.html',{'result':result})

def interface_casetest_result(request,aid):
    print(aid)
    result_data = createinterfacetest.objects.filter(Q(usercaseID=aid))
    return render(request,'interface_test_case.html',{'result':result_data,'usercaseID':aid})


def interface_test_result(request):
    caseID = request.GET.get('caseID')
    name = request.GET.get('name')
    method = request.GET.get('method')
    URL = request.GET.get('URL')
    param = request.GET.get('param')
    eresults = request.GET.get('eresults')
    Actualoutput = request.GET.get('Actualoutput')
    testresult = request.GET.get('testresult')

    if method == 'get':
        print('1234')
        requ = requests.get(URL+'?'+param)


    elif method == 'POST':
        print('234')
        requ = requests.post(URL+'?'+param)

    # print(caseID,name,method,URL,param,eresults,Actualoutput,testresult)
    cID = createinterfacetest.objects.get(caseID=caseID)
    cID.Actualoutput = requ.text
    cID.eresults = eresults
    cID.save()
    if createinterfacetest.objects.filter(Q(Actualoutput__contains=eresults)).exists():
        cID = createinterfacetest.objects.get(caseID=caseID)
        cID.testresult = '成功'
        cID.save()

        # testresult = '成功'
    # if eresults == requ.text:
    #     testresult = '成功'
    else:
        cID = createinterfacetest.objects.get(caseID=caseID)
        cID.testresult = '失败'
        cID.save()
    result = createinterfacetest.objects.all()
    return render(request, 'interface_test_case.html', {'result': result})

def batch(request,aid):
    # print(aid)
    result_data = createinterfacetest.objects.filter(Q(usercaseID=aid))
    for result in result_data:
        # print(result.caseID,result.name,result.method,result.URL,result.contentType,result.param,result.Actualoutput,result.eresults,result.testresult)
        if result.method == 'get':
            # print('1234')
            r = requests.get(result.URL+'?'+result.param)
        elif result.method == 'POST':
            # print('234')
            r = requests.post(result.URL+'?'+result.param)
        cID = createinterfacetest.objects.get(caseID=result.caseID)
        cID.Actualoutput = r.text
        cID.eresults = result.eresults
        cID.save()
        if createinterfacetest.objects.filter(Q(Actualoutput__contains=result.eresults)).exists():
            cID = createinterfacetest.objects.get(caseID=result.caseID)
            cID.testresult = '成功'
            cID.save()

            # testresult = '成功'
        # if eresults == requ.text:
        #     testresult = '成功'
        else:
            cID = createinterfacetest.objects.get(caseID=result.caseID)
            cID.testresult = '失败'
            cID.save()
        result = createinterfacetest.objects.all()
    rs = Use_case_management.objects.all()
    return render(request,'usecasemanagement.html',{'result':rs})


def monkeytest(request):
    cm = PythonAdb.get_devices(request)
    print(cm)
    return render(request,'monkeytest.html',{'cm':cm})

def operator(request):
    L = []
    cm=request.GET.get('name','')
    L.append(request.GET.get('p',''))
    L.append(request.GET.get('r',''))
    L.append(request.GET.get('t',''))
    L.append(request.GET.get('vt',''))
    L.append(request.GET.get('m',''))
    L.append(request.GET.get('lj',''))

    # print(' '.join(L))
    a = ' '.join(L)
    # print(a)
    PythonAdb(a).adb_operator()
    # print(cm)
    return render(request,'monkeytest.html',{'cm':cm})

def performan(request):
    a = 'com.yunfang.eias'
    print(a)
    PyPerforman(a).Per_cpu()
    PyPerforman(a).Per_men()
    return render(request,'all_info.html')

#新版本
def interfaceTest(request):
    return render(request,'index1.html')

def charts(request):
    return render(request,'charts.html')

def widgets(request):
    return render(request,'widgets.html')


def report_list(request):
    result_list = result_test_runss.objects.all()

    return render(request,'report_list.html',{'events':result_list})

def tables(request):
    return render(request,'tables.html')

def grid(request):
    return render(request,'grid.html')

def form_common(request):
    return render(request,'form-common.html')

def form_validation(request):
    return render(request,'form-validation.html')

def form_wizard(request):
    return render(request,'form-wizard.html')

def buttons(request):
    return render(request,'buttons.html')

def Eelements(request):
    return render(request,'Eelements.html')

def index2(request):
    return render(request,'index2.html')

def gallery(request):
    return render(request,'gallery.html')

def calendar(request):
    return render(request,'calendar.html')

def invoice(request):
    return render(request,'invoice.html')

def chat(request):
    return render(request,'chat.html')

def error403(request):
    return render(request,'error403.html')

def error404(request):
    return render(request,'error404.html')

def error405(request):
    return render(request,'error405.html')

def error500(request):
    return render(request,'error500.html')


def get_event_list(request):

    eid = request.GET.get("eid", "")      # 发布会id
    name = request.GET.get("name", "")    # 发布会名称

    if eid == '' and name == '':
        return JsonResponse({'status':10021,'message':'parameter error'})

def WebUIindex(request):
    result = new_item.objects.all()
    return render(request,'WebUIindex.html',{'result':result})

def add_item(request):
    return render(request,'add_item.html')

def new_items(request):
    itemname = request.GET.get('itemname')
    itemdescript = request.GET.get('itemdescript')
    createname = request.session.get('username', '')
    new_item.objects.create(itemName=itemname,itemdescript=itemdescript,createname=createname)
    result = new_item.objects.all()
    return render(request,'WebUIindex.html',{'result':result})

def descript(request,aid):
    result = new_item.objects.get(id=aid)
    return render(request,'itemdescript.html',{'result':result})

def itemcreate(request,aid):
    result = new_item.objects.get(id=aid)
    newresult = add_item_case_set.objects.filter(Q(newitemID=aid))
    return render(request,'itemlist.html',{'result':result,'newresult':newresult})


def itemdelete(request,aid):
    result = new_item.objects.get(id=aid)
    result.delete()
    return HttpResponseRedirect('/WebUI/')

def itemcaseset(request,aid):
    result = new_item.objects.get(id=aid)
    return render(request,'item_case_set.html',{'result':result})

def itemcasesetcreate(request,aid):
    casesetName = request.GET.get('casesetName','')
    casesetdescript = request.GET.get('casesetdescript','')
    createname = request.session.get('username', '')
    add_item_case_set.objects.create(newitemID=aid,casesetName=casesetName,createname=createname,casesetdescript=casesetdescript)
    newresult = add_item_case_set.objects.all()
    return render(request,'itemlist.html',{'newresult':newresult})

def case(request,aid):
    # result = uicase.objects.get(itemID=aid)
    result = uicase.objects.filter(Q(itemID=aid))
    return render(request, 'case.html', {'newresult': result,'id':aid})
    # print(aid)
    # return render(request, 'case.html', {'id':aid})


def casesteps(request,aid):
    ad = add_item_case_set.objects.get(id=aid)
    return render(request,'casestep.html',{'id':aid,'ad':ad})

def casestep_new(request):
    itemID = request.GET.get('itemID','')
    Versionnumber = request.GET.get('Version_number','')
    casename = request.GET.get('casename','')
    casesetName = request.GET.get('casesetName','')
    ScriptType = request.GET.get('ScriptType','')
    Label = request.GET.get('Label','')
    descript = request.GET.get( 'descript','')
    print(itemID,Versionnumber,casename,casesetName,ScriptType,Label,descript)
    if uicase.objects.filter(Q(casename=casename)& Q(itemID=itemID)).exists():
        print('已存在数据')
    else:
        uicase.objects.create(itemID=itemID,Versionnumber=Versionnumber,casename=casename,casesetName=casesetName,ScriptType=ScriptType,Label=Label,descript=descript)
    result = uicase.objects.filter(Q(itemID=request.GET.get('itemID','')))
    return HttpResponseRedirect('/itemlist/step/'+itemID+'/d/',{'newresult':result})

def casestep_edit(request,aid):
    # print(aid)
    result = uicase.objects.get(id=aid)
    # print(result.id,result.casename,result.itemID)
    return render(request,'casestepeidt.html',{'id':aid,'itemID':result.itemID,'casename':result.casename,
                                               'Versionnumber':result.Versionnumber,'casesetName':result.casesetName,
                                               'ScriptType':result.ScriptType,'Label':result.Label,'descript':result.descript})

def casestep_edit_create(request,aid):
    # print(aid)
    itemID = request.GET.get('itemID', '')
    Versionnumber = request.GET.get('Version_number', '')
    casename = request.GET.get('casename', '')
    casesetName = request.GET.get('casesetName', '')
    ScriptType = request.GET.get('ScriptType', '')
    Label = request.GET.get('Label', '')
    descript = request.GET.get('descript', '')
    # print(itemID,Versionnumber,casename,casesetName,ScriptType,Label,descript)
    uicase.objects.filter(id=aid).update(itemID=itemID,Versionnumber=Versionnumber,casename=casename,casesetName=casesetName,ScriptType=ScriptType,Label=Label,descript=descript)
    # uicase.objects.update(itemID=itemID,Versionnumber=Versionnumber,casename=casename,casesetName=casesetName,ScriptType=ScriptType,Label=Label,descript=descript)
    result = uicase.objects.filter(Q(itemID=request.GET.get('itemID', '')))
    return render(request, 'case.html', {'newresult': result})

def newcasestep(request,aid):
    print(aid)
    uicase_result = uicase.objects.filter(id=aid)
    for i in uicase_result:
        add_result = add_item_case_set.objects.filter(id=i.itemID)
        for n in add_result:
           new_item_result = new_item.objects.filter(id=n.newitemID)
           for ne in new_item_result:
                 print(ne.itemName)
        # print(i.itemID)
        # key = uicase.objects.filter(itemID=i.itemID)
        # for k in key:
        #     print(k.itemID,k.casename)
    keyresult = uicase.objects.filter(itemID=uicase_result.get(id=aid).itemID)

    result = casestep.objects.filter(Q(itemID=aid))
    return render(request,'newcasestep.html',{'id':aid,'itemname':ne.itemName,'casesetName':n.casesetName,'result':result,'keyword':keyresult})

def casestepcreate(request,aid):
    stepID = request.GET.get('stepID')
    kword = request.GET.get('kword')
    Roadking = request.GET.get('Roadking')
    Param = request.GET.get('Param')
    Descript = request.GET.get('Descript')
    casestep.objects.create(caseID=stepID,itemID=aid,kword=kword,Roadking=Roadking,Param=Param,Descript=Descript)
    result = casestep.objects.filter(Q(itemID=aid))
    return HttpResponseRedirect('/newcasestep/'+aid+'/d/',{'result':result})


y = 0
k = []
b = []
m = []
def caserun(request,aid):
    print(aid)
    # new = casestep.objects.filter(Q(itemID=aid))
    new = casestep.objects.filter(Q(itemID=aid))
    for n in new:
        if n.kword.lower() == 'Open'.lower():
            browser = location.open(n.Roadking, n.Param)
            b.append(browser)
            # print(b[0])
        elif n.kword.lower() == 'Input_Text'.lower():
            location.Input_Text(browser, n.Roadking, n.Param)
            time.sleep(10)
        elif n.kword.lower() == 'New_Click'.lower():
            # print(b[0])
            if b[0] is not None:
                location.New_Click(browser, n.Roadking)
            elif m[0]is not None:
                print(k[0])
                location.New_Click(k[0], n.Roadking)
            time.sleep(38)
        elif n.kword.lower() == 'new_browser_close'.lower():
            time.sleep(5)
            location.new_browser_close(browser)
        elif uicase.objects.filter(Q(casename=n.kword)).exists():
            # print(n.itemID)
            # lzq = uicase.objects.filter(id=n.itemID)
            # for ll in lzq:
            #     print(ll.itemID)
            browser = new2(aid,n.kword)
            m.append(browser)



    result = casestep.objects.all()
    return HttpResponseRedirect('/newcasestep/' + aid + '/d/', {'result': result})

# def new1 (new):
#     for n in new:
#         if n.kword.lower() == 'Open'.lower():
#             browser = location.open(n.Roadking, n.Param)
#         elif n.kword.lower() == 'Input_Text'.lower():
#             location.Input_Text(browser, n.Roadking, n.Param)
#             time.sleep(10)
#         elif n.kword.lower() == 'New_Click'.lower():
#             location.New_Click(browser, n.Roadking)
#             time.sleep(38)
#         elif n.kword.lower() == 'new_browser_close'.lower():
#             location.new_browser_close(browser)

def new2(aid,new,m=None):
    print(aid,new)
    print('吕梓清')
    if uicase.objects.filter(Q(casename=new)).exists():
        lzq = uicase.objects.filter(id=aid)
        n = uicase.objects.filter(itemID=lzq.get(id=aid).itemID).get(casename=new)
        # n = uicase.objects.get(casename=new)
        # n = uicase.objects.get(casename=new)
        print(n.id,n.casename)
        new = casestep.objects.filter(Q(itemID=n.id))

        for n in new:
            print(n.kword)
            if n.kword.lower() == 'Open'.lower():
                browser = location.open(n.Roadking, n.Param)
                k.append(browser)


            elif n.kword.lower() == 'Input_Text'.lower():
                print('黄远阜')
                location.Input_Text(k[y-1], n.Roadking, n.Param)
                time.sleep(10)
            elif n.kword.lower() == 'New_Click'.lower():
                print('黄')
                browser = location.New_Click(k[y-1], n.Roadking)
                time.sleep(38)
            elif n.kword.lower() == 'new_browser_close'.lower():
                location.new_browser_close(k[y-1])
            print(k[0])

        return k[0]

def runcase(request,aid):
    name = uicase.objects.get(id=aid).casename
    print(name)
    test_app = "./web"  # 定义测试应用
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(test_app + "/report/" + now_time + "result.html", 'wb')
    runner = HTMLTestRunner(fp,
                            title="xxx测试报告",
                            description="运行环境：%s, %s" % (platform.system(), "Chrome"))
    # discover = unittest.defaultTestLoader.discover(test_app + "/test_case", pattern='*_case.py')
    suiteTest = unittest.TestSuite()
    # h=MyTestCase().__getattr__('testCase1')
    name =aid +name
    print(name)
    suiteTest.addTest(MyTestCase(name))

    # suiteTest.addTest(MyTestCase("testCase1"))
    # suiteTest.addTest(MyTestCase("退出"))
    # suiteTest.addTest(MyTestCase("注册"))
    # suiteTest.addTest(MyTestCase("testCase3"))
    runner.run(suiteTest)
    fp.close()
    result = uicase.objects.filter(Q(itemID=aid))
    return render(request, 'case.html', {'newresult': result, 'id': aid})


def Modular1(aid,kword):


    # location.New_Click(driver,"xpath=.//*[@id='expmenu-freebie']/li/ul/li[1]/ul/li[1]/a")
    # new = casestep.objects.filter(Q(itemID=aid))
    # for n in new:
    newid = uicase.objects.filter(Q(casename=kword))
        # print(n.kword)
    # for new in newid:
    new1(newid.get(id))
            # print(new.id)
            # Modular(new.id)
            # browser = new.casename
            # print(browser)
            # Modular(aid)



def Modular(aid):
    '''
    模块
    '''
    print(aid)
    new = casestep.objects.filter(Q(itemID=aid))
    k = []
    i = 0
    for n in new:
        print(n.id)
        # for i in n.id:
        print(n.kword)
        if n.kword.lower() == 'Open'.lower():
            browser = location.open(n.Roadking, n.Param)
            k.append(browser)
            print(k[0])

        # elif n.kword.lower() == 'Input_Text'.lower():
        #     print(i)
            # print(k[0])
            # browser = k[0]
            # location.Input_Text(k[0], n.Roadking, n.Param)
        # elif n.kword.lower() == 'New_Click'.lower():
        #     location.New_Click(browser, n.Roadking)
        #     time.sleep(10)
        i = i+1
    # return browser


def analysis(request):

    d ={
        '1.hldxhzj.duapp.com':9397,
        'www.xxx.com':777,
    }

    plt.figure(figsize=(8,6),dpi=80)
    cataegories = d.keys()
    data = d.values()
    return render(request, "Analysis.html",{'user':request.user,'cataegories':cataegories,'data':data})





def simple(request):

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return render(request,'Analysis.html',canvas.print_png(response))


def show_result(request):
    """draw result image"""
    import matplotlib_util
    from Py3ForRfResultAnalysis.settings import MEDIA_ROOT

    # draw histogram
    n_groups = Question.objects.all().count()
    options = ('A', 'B', 'C', 'D')
    nums = []
    for option in options:
        num = []
        for tid in range(1, n_groups + 1):
            cnt = Result.objects.filter(t_id=tid, my_option=option).count()
            num.append(cnt)
        nums.append(num)
    histogram_path = MEDIA_ROOT + 'images\\results\\' + '0.png'
    print (histogram_path)
    try:
        matplotlib_util.draw_histogram(nums[0], nums[1], nums[2], nums[3],
                                      n_groups, histogram_path)
    except:    # handle all exception
        return render(request, 'result_image.html',
                      {'images': None})

    # draw pie chart
    for tid in range(1, n_groups+1):
        explode = [0.0, 0.0, 0.0, 0.0]
        answer_num = ord(Question.objects.get(t_id=tid).t_answer.upper()) - ord('A')
        explode[answer_num] = 0.1
        explode = tuple(explode)

        question_info = []
        for each in options:
            cnt = Result.objects.filter(t_id=tid, my_option=each).count()
            question_info.append(cnt)

        chart_path = MEDIA_ROOT + 'images\\results\\' + str(tid) + '.png'
        print (chart_path)
        try:
            matplotlib_util.draw_piechart(question_info, explode, chart_path)
        except:
            return render(request, 'result_image.html',
                          {'images': None})

    images = []
    for i in range(n_groups+1):
        images.append('/media/images/results/'+str(i)+'.png')
    return render(request, 'result_image.html', {'images': images})




