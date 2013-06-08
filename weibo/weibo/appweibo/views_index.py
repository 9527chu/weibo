#coding:utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from weibo.appweibo.models import *
import random

class LoginForm(forms.Form):
    '''注册表单'''
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

def index(request):
    """ Index page """
    topics = Topic.objects.all()
    users = User.objects.exclude(username=request.user.username).exclude(username='root') 
    show_users = []
   # while len(show_users) < 2:  #随机产生2个用户，推荐收听
    for var_i in xrange(3):   #随机产生最多3个
        if users:
            user = random.choice(users)
            if user not in show_users:
                if request.user.is_authenticated():
                    if user not in request.user.get_profile().follow.all(): #登录后选出不是自己已关注的人
                        show_users.append(user)
                else:
                    show_users.append(user)
                
    weibos = Weibo.objects.all().order_by('-id')
    loginform = LoginForm()
    content = {
        'weibos': weibos,
        'request': request,
        'topics': topics,
        'loginform': loginform,
        'show_users': show_users,
    } 
    return render_to_response('index.html', content)

