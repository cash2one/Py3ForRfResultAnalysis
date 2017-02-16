from selenium import webdriver
import os
import time

class function(object):
    def insert_img(self,driver, file_name):
        #base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = os.getcwd()
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('/web')[0]
        file_path = base + "/web/report/image/" + file_name
        print(file_path)
        driver.get_screenshot_as_file(file_path)

    def Generate_picture(self,browser,name=None):
        time.sleep(3)
        img_id = self.image_id()
        if name is not None:
            file_name = name +".jpg"
        else:
            file_name = img_id + ".jpg"
        function().insert_img(browser, file_name)
        print("image/" + file_name)

    global case_count
    case_count = 0

    global image_count
    image_count = 0

    # 计算测试用例的个数，用于显示在测试报告中
    def case_id(self):
        global case_count
        case_count += 1
        if case_count <= 9:
            count = "00" + str(case_count)
        elif case_count <= 99:
            count = "0" + str(case_count)
        else:
            count = str(case_count)
        return count

    # 测试完成，生成截图文件的名称
    def image_id(self):
        global image_count
        image_count += 1
        if image_count <= 9:
            count = "00" + str(image_count)
        elif image_count <= 99:
            count = "0" + str(image_count)
        else:
            count = str(image_count)
        return count





# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# function().insert_img(driver, 'baidu.jpg')
# driver.quit()
