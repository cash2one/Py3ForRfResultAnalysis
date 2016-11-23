"""Py3ForRfResultAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',views.login_action),
    url(r'^logout/$',views.logout),
    url(r'^index/$', views.index),
    url(r'^sreach_name/$', views.sreach_name),
    url(r'^del_data/(?P<aid>\d+)/d/$',views.del_data),
    url(r'^analysis/$',views.simple),
    url(r'^analysis/columnar_analysic/$', views.columnar_analysic),
    url(r'^sreach_name/result/$', views.sreach_name_result),
    url(r'^database/$',views.databascon),
    url(r'^database/connection/$',views.databasconn),
    url(r'^database/createdata/$', views.data_create),
    url(r'^TestTools/$',views.show_result),


]
