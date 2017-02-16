#coding=utf-8
from selenium import webdriver

'''
文本简易封装定位单个元素和定位一组元素方法
'''

'''定位当个元素封装'''

def Browser(driver):
    if driver.lower() == 'Chrome'.lower():
        browser = webdriver.Chrome()
    elif driver.lower() == 'Firefox'.lower():
        browser = webdriver.Firefox()
    elif driver.lower() == 'Ie'.lower():
        browser = webdriver.Ie()
    return browser

def open(driver,url):
    '''
    打开浏览器，需要参数：浏览器驱动、链接地址
    '''
    browser = Browser(driver)
    browser.get(url)
    browser.maximize_window()
    return browser

def new_browser_close(driver):
    driver.quit()

def close(driver):
    driver.quit()

def findID(driver,id):
    '''根据ID号进行查找，参数：驱动、id'''
    f = driver.find_element_by_id(id)
    return f

def findName(driver,name):
    f = driver.find_element_by_name(name)
    return f

def findClassName(driver,classname):
    f = driver.find_element_by_class_name(classname)
    return f

def findCss(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f

def findTagName(driver,tag):
    print(tag)
    f = driver.find_element_by_tag_name(tag)
    return f

def findLinkText(driver,text):
    f = driver.find_element_by_link_text(text)
    return f

def findXpath(driver,xpath):
    print(xpath)
    f = driver.find_element_by_xpath(xpath)
    return f

def Input_Text(driver,xpath,text):
    '''输入参数'''
    kk = xpath.split('=')
    if kk[0].lower() == 'id'.lower():
        return findID(driver,kk[1]).send_keys(text)
    elif kk[0].lower() == 'name'.lower():
        return findName(driver,kk[1]).send_keys(text)
    elif kk[0].lower() == 'class'.lower():
        return findClassName(driver,kk[1]).send_keys(text)
    elif kk[0].lower() == 'css'.lower():
        return findCss(driver,kk[1]).send_keys(text)
    elif kk[0].lower() == 'xpath'.lower():
        kk = list(xpath)[6:]
        kk[1] = ''.join(kk)
        return findXpath(driver,kk[1]).send_keys(text)

def Get_Text(driver,xpath):
    '''获取页面内容'''
    kk = xpath.split('=')
    if kk[0].lower() == 'id'.lower():
        return findID(driver, kk[1]).text
    elif kk[0].lower() == 'name'.lower():
        return findName(driver, kk[1]).text
    elif kk[0].lower() == 'class'.lower():
        return findClassName(driver, kk[1]).text
    elif kk[0].lower() == 'css'.lower():
        return findCss(driver, kk[1]).text
    elif kk[0].lower() == 'xpath'.lower():
        kk = list(xpath)[6:]
        kk[1] = ''.join(kk)
        return findXpath(driver, kk[1]).text

def Get_Value(driver,xpath):
    '''获取输入框内容'''
    kk = xpath.split('=')
    if kk[0].lower() == 'id'.lower():
        return findID(driver, kk[1]).get_attribute("value")
    elif kk[0].lower() == 'name'.lower():
        return findName(driver, kk[1]).get_attribute("value")
    elif kk[0].lower() == 'class'.lower():
        return findClassName(driver, kk[1]).get_attribute("value")
    elif kk[0].lower() == 'css'.lower():
        return findCss(driver, kk[1]).get_attribute("value")
    elif kk[0].lower() == 'xpath'.lower():
        kk = list(xpath)[6:]
        kk[1] = ''.join(kk)
        return findXpath(driver, kk[1]).get_attribute("value")

def New_Click(driver,xpath):
    kk = xpath.split('=')
    if kk[0].lower() == 'id'.lower():
        return findID(driver, kk[1]).click()
    elif kk[0].lower() == 'name'.lower():
        return findName(driver, kk[1]).click()
    elif kk[0].lower() == 'class'.lower():
        return findClassName(driver, kk[1]).click()
    elif kk[0].lower() == 'css'.lower():
        return findCss(driver, kk[1]).click()
    elif kk[0].lower() == 'xpath'.lower():
        kk = list(xpath)[6:]
        kk[1] = ''.join(kk)
        return findXpath(driver, kk[1]).click()






