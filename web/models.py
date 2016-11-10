from django.db import models
import os

# Create your models here.

# class Person_registered(models.Model):
#     '''注册用户表'''
#     username = models.CharField('姓名', max_length=64, blank=True, null=False)
#     password = models.CharField('密码', max_length=128)
#     birth_date = models.DateField('出生日期')
#     address = models.CharField('地址',max_length=255)
#     city = models.CharField('城市',max_length=50)
#
#     def __str__(self):
#         return self.username
#
# class Userprofile(models.Model):
#     '''用户信息表'''
#     username = models.CharField('姓名',max_length=64,blank=True,null=False)
#
#
#     def __str__(self):
#         return self.username


class dict_test_case(models.Model):
    id = models.IntegerField(default=11,primary_key = True)
    caseName = models.CharField(max_length=255,blank=True,null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=255)
    status = models.IntegerField(default=11,blank=True,null=False)
    caseType = models.CharField(max_length=255)

    def __unicode__(self):
        return self.caseName


class dict_test_data(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    dataContent = models.CharField(max_length=255)
    dataName = models.CharField(max_length=255)
    caseId = models.IntegerField(default=11)
    groupID = models.IntegerField(default=11)

    def __unicode__(self):
        return self.dataName

class result_arguments(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    keyword_id = models.IntegerField(default=10)
    content = models.TextField()

    def __unicode__(self):
        return self.content,self.keyword_id

class result_keyword_status(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    keyword_id = models.IntegerField(default=10)
    status = models.TextField()
    elapsed = models.IntegerField(default=255)

    def __unicode__(self):
        return  self.keyword_id,self.status

class result_keywords(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    suite_id = models.IntegerField(default=10)
    test_id = models.IntegerField(default=10)
    keyword_id = models.IntegerField(default=10)
    name = models.TextField()
    type = models.TextField()
    timeout = models.TextField()
    doc = models.TextField()

    def __unicode__(self):
        return  self.name

class result_messages(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    keyword_id = models.IntegerField(default=10)
    level = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.keyword_id,self.timestamp

class result_suite_status(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    suite_id = models.IntegerField(default=10)
    elapsed = models.IntegerField(default=255)
    failed = models.IntegerField(default=3)
    passed = models.IntegerField(default=3)
    status = models.TextField()

    def __unicode__(self):
        return self.suite_id,self.failed,self.passed,self.status

class result_suites(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    suite_id = models.IntegerField(default=10)
    xml_id = models.TextField()
    name = models.TextField()
    source = models.TextField()
    doc = models.TextField()

    def __unicode__(self):
        return  self.name,self.source

class result_tag_status(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    name = models.TextField()
    critical = models.IntegerField(default=1)
    elapsed = models.IntegerField(default=255)
    failed = models.IntegerField(default=3)
    passed = models.IntegerField(default=3)

    def __unicode__(self):
        return self.name,self.failed,self.passed

class result_tags(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_id = models.IntegerField(default=10)
    content = models.TextField()

    def __unicode__(self):
        return self.test_id

class result_test_run_errors(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    level = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.test_run_id

class result_test_run_status(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    name = models.TextField()
    elapsed = models.IntegerField(default=255)
    failed = models.IntegerField(default=3)
    passed = models.IntegerField(default=3)

    def __unicode__(self):
        return self.name,self.failed,self.passed

class result_test_runss(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    source_file = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now_add=True)
    hash = models.TextField()
    imported_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.source_file

class result_test_status(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    test_run_id = models.IntegerField(default=10)
    test_id = models.IntegerField(default=10)
    status = models.TextField()
    elapsed = models.IntegerField(default=255)

    def __unicode__(self):
        return self.test_id,self.status,self.elapsed

class result_tests(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    suite_id = models.IntegerField(default=10)
    xml_id = models.TextField()
    name = models.TextField()
    timeout = models.DateTimeField(auto_now_add=True)
    doc = models.TextField()

    def __unicode__(self):
        return self.name

class Result(models.Model):
        """Question result info."""
        t_id = models.IntegerField(u'题号')
        user_num = models.CharField(u'学号', max_length=30)
        my_option = models.CharField(u'答案', max_length=10)

        def __unicode__(self):
            ans_str = self.t_id + self.my_option
            return ans_str

        class Meta:
            ordering = ['t_id', 'user_num']

def get_image_path(instance, filename):
    return os.path.join('images', instance.t_id, filename)

class Question(models.Model):
    """Question Info"""
    t_id = models.IntegerField(u'题号', primary_key=True)
    t_content = models.TextField(u'题目', blank=True)
    t_answer = models.CharField(u'答案', max_length=1)
    a_select_users = models.IntegerField(u'选A人数', default=0)
    b_select_users = models.IntegerField(u'选B人数', default=0)
    c_select_users = models.IntegerField(u'选C人数', default=0)
    d_select_users = models.IntegerField(u'选D人数', default=0)
    t_option1 = models.TextField(u'选项A', blank=True)
    t_option2 = models.TextField(u'选项B', blank=True)
    t_option3 = models.TextField(u'选项C', blank=True)
    t_option4 = models.TextField(u'选项D', blank=True)
    t_image = models.ImageField(u'Image', upload_to=get_image_path, blank=True)

    def __unicode__(self):
        ret_str = self.t_id + self.t_answer
        return ret_str


























