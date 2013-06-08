#coding:utf8
from django.conf.urls import patterns, include, url
import os


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weibo.views.home', name='home'),
    # url(r'^weibo/', include('weibo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$', 'weibo.appweibo.views_index.index'),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/js")},name='js'),
    url(r'css/(?P<path>[\w\.\-]+\.css)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/css")},name='css'),
    url(r'images/(?P<path>[\w\.\-]+\.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/images")},name='images'),

    url(r'media/(?P<path>[\w\.\-]+\.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./mymedia")},name='media'),
)

urlpatterns += patterns('',
    url(r'^$', 'weibo.appweibo.views_index.index', name='index'), ## 张凌阁
    url(r'^index/', include('weibo.appweibo.urls_index')), ## 张凌阁
    url(r'^topic/', include('weibo.appweibo.urls_topic')), ## 
    url(r'^myhome/', include('weibo.appweibo.urls_myhome')), ## 
    #url(r'^funs/', include('weibo.appweibo.urls_funs')), ## 何震雄
    url(r'^regist/', include('weibo.appweibo.urls_regist')), ## 
    url(r'^search/', include('weibo.appweibo.urls_search')), ## 
    url(r'^follow/', include('weibo.appweibo.urls_follow')), ##张春龙 
    url(r'^home/', include('weibo.appweibo.urls_home')), ##杨志雨  
    url(r'^setting/', include('weibo.appweibo.urls_setting')), ##高志成

    url(r'^public/', include('weibo.appweibo.urls_public')),    # xcluo
)


