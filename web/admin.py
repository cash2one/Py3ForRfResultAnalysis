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

admin.site.register(result_test_runs, ResultAdmin)