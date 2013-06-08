#-*- coding:utf8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('weibo.appweibo.views_public',
    url(r'^weibo/add/$', 'weibo_add', name='weibo_add'),    # 发微博， 使用POST提交, 包含一个标签textarea：name=context
    url(r'^lgoin/exe/$', 'ulogin', name='login'),    # 登录, 是用POST ,标签username,password
    url(r'^logout/$', 'ulogout', name='logout' ),# 注销
    url(r'^weibo/reply/(\d+)/$', 'weibo_reply', name='reply'),# 评论微波页面
    url(r'^weibo/reply_add/(\d+)/$', 'weibo_reply_add', name='reply_add'),# 发评论
    url(r'weibo/collect_add/(\d+)/$', 'collect_add', name='collect_add'),#收藏
    url(r'^weibo/collect/$', 'collect', name='collect'), #查看收藏
    url(r'^weibo/forwarding/(\d+)/$', 'forwarding', name='forwarding'), #查看收藏
    url(r'^weibo/forwarding_add/(\d+)/$', 'forwarding_add', name='forwarding_add'), #添加收藏
    url(r'^weibo/follow_add/(\d+)/$', 'follow_add', name='follow_add'), #添加关注
)


#  action='{% url weibo_add %}'


