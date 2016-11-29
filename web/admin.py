from django.contrib import admin
from web.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'source_file', 'started_at','finished_at','hash','imported_at']
    search_fields = ['source_file']    # 搜索功能
    list_filter = ['source_file']    # 过滤器

class ResultStatueAdmin(admin.ModelAdmin):
    list_display = ['id','test_run_id','name','elapsed','failed','passed']
    search_fields = ['test_run_id']
    list_filter = ['test_run_id']

class DatacreateAdmin(admin.ModelAdmin):
    list_display = ['name','IP_Address','Port','username','password']
    search_fields = ['name']
    list_filter = ['name']



admin.site.register(result_test_run_status,ResultStatueAdmin)
admin.site.register(result_test_runss, ResultAdmin)
admin.site.register(create_data,DatacreateAdmin)