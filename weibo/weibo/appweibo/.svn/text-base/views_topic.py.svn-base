''' views  '''
#coding:utf8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from weibo.appweibo.models import *
from django import forms
import os, re, math, random
class LoginForm(forms.Form):
    '''注册表单'''
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
class WeiboForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea, required=False, label='',)
def re_re(request,uid):
    ''' 获取用户点击的热门话题，并转到该热门话题的主页 ''' 
    topic = Topic.objects.get(id=uid)
    weibos = topic.weibo.all() 
    title = topic.title
    users = User.objects.exclude(username=request.user.username).exclude(username='root')
    show_users = []
    for var_i in xrange(4):   #随机产生最多3个
        if users:
            user = random.choice(users)
            if user not in show_users:
                if request.user.is_authenticated():
                    if user not in request.user.get_profile().follow.all(): #登录后选出不是自己已关注的人
                        show_users.append(user)
                else:
                    show_users.append(user)
    text = topic.weibo.all().order_by('id')[0].context
    topics = Topic.objects.exclude(title=topic)
    title = topic.title
    loginform = LoginForm()
    weiboform = WeiboForm(initial={'context':'#'+title+'#'})
    return render_to_response('show_topic.html', {'text':text,'weiboform':weiboform, 'request':request,'loginform':loginform,'weibos':weibos, 'title':title, 'topics':topics,'show_users':show_users, 'topic':topic})






































