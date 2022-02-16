
from django.urls import path
from django.conf.urls import url
from apps.test_service import views

'''
This file contains routing information. It maps URL-Patterns to view-functions in the "views.py"
'''


urlpatterns = [
    url(r'^tests/(?P<test_id>\d+)/$', views.get_test, name='testdetails'),
    url(r'^deletetest/(?P<test_id>\d+)/$', views.delete_test, name='testdelete'),
    #path('test/<int:id>/', views.get_test, name="testoverview"),
    path('testoverview/', views.test_overview, name='testoverview'),
    path('addnewfiotest/', views.new_fio_test, name='newfiotest'),
    path('addnewiperf3test/', views.new_iperf3_test, name='newiperf3test'),
    path('addnewpgbenchtest/', views.new_pg_bench_test, name='newpgbenchtest'),
    path('', views.home, name='index'),
    url(r'^testevents/(?P<test_id>\d+)/$', views.get_events_for_test, name='testevents'),

]