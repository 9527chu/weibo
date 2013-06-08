#-*- coding:utf8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('weibo.appweibo.views_myhome',
    url(r'^myhome/$', 'myhome', name='myhome_myhome'), 

)

