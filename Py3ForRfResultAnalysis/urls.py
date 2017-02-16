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
    url(r'^database/operation/$', views.data_operation),
    url(r'^monkeytest/$', views.monkeytest),
    url(r'^monkeytest/operator/$', views.operator),
    url(r'^monkeytest/performan/$', views.performan),
    url(r'^TestTools/$',views.show_result),
    url(r'^interfaceTest/$',views.interfaceTest),

    #其他
    url(r'^charts/$', views.charts),
    url(r'^widgets/$', views.widgets),
    url(r'^report_list/$', views.report_list),
    url(r'^rep_del_data/(?P<aid>\d+)/d/$', views.rep_del_data),
    url(r'^report_graph_analysis/$', views.report_graph_analysis),
    url(r'^database_list/$', views.database_list),
    url(r'^create_interfacetest/$', views.create_interfacetest),
    url(r'^new_interfacetest/$', views.new_interfacetest),
    url(r'^new_interfacetest/(?P<aid>\d+)/d/$', views.new_interfacetest_id),
    url(r'^new_interfacetest/new/(?P<aid>\d+)/d/$', views.new_interfacetest_new),
    url(r'^interface_test_case/$', views.interface_test_case),
    url(r'^usecasemanagement/$', views.usecasemanagement),
    url(r'^newcaseaggregate/$', views.newcaseaggregate),
    url(r'^interface_test_case/result/$', views.interface_test_result),
    url(r'^interface_test_case/result/(?P<aid>\d+)/d/$', views.interface_casetest_result),
    url(r'^interface_test_case/batch/(?P<aid>\d+)/d/$', views.batch),
    url(r'^tables/$', views.tables),
    url(r'^grid/$', views.grid),
    url(r'^form_common/$', views.form_common),
    url(r'^form_validation/$', views.form_validation),
    url(r'^form_wizard/$', views.form_wizard),
    url(r'^buttons/$', views.buttons),
    url(r'^Eelements/$', views.Eelements),
    url(r'^index2/$', views.index2),
    url(r'^gallery/$', views.gallery),
    url(r'^calendar/$', views.calendar),
    url(r'^invoice/$', views.invoice),
    url(r'^chat/$', views.chat),
    url(r'^error403/$', views.error403),
    url(r'^error404/$', views.error404),
    url(r'^error405/$', views.error405),
    url(r'^error500/$', views.error500),

    url(r'^get_event_list/$', views.get_event_list),

    #自动化平台
    url(r'^WebUI/$', views.WebUIindex),
    url(r'^add_item/$', views.add_item),
    url(r'^new_item/$', views.new_items),
    url(r'^WebUIindex/descript/(?P<aid>\d+)/d/$', views.descript),
    url(r'^WebUIindex/create/(?P<aid>\d+)/d/$', views.itemcreate),
    url(r'^WebUIindex/delete/(?P<aid>\d+)/d/$', views.itemdelete),
    url(r'^add_item_case_set/(?P<aid>\d+)/d/$', views.itemcaseset),
    url(r'^add_item_case_set/itemcaseset/(?P<aid>\d+)/d/$', views.itemcasesetcreate),
    url(r'^itemlist/step/(?P<aid>\d+)/d/$', views.case),
    url(r'^add_case_step/(?P<aid>\d+)/d/$', views.casesteps),
    url(r'^add_case_step/create/$', views.casestep_new),
    url(r'^edit/(?P<aid>\d+)/d/$', views.casestep_edit),
    url(r'^edit/create/(?P<aid>\d+)/d/$', views.casestep_edit_create),
    url(r'^newcasestep/(?P<aid>\d+)/d/$', views.newcasestep),
    url(r'^newcasestep/run/(?P<aid>\d+)/d/$', views.caserun),
    url(r'^newcasestep/create/new/(?P<aid>\d+)/d/$', views.casestepcreate),
    url(r'^case/(?P<aid>\d+)/d/$', views.runcase),



    # url(r'^itemlist/casestep/(?P<aid>\d+)/d/$', views.casestep),






]
