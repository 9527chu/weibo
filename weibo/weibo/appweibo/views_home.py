#-*- coding:utf8 -*-
#显示用户主页
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from weibo.appweibo.models import *
import random
class WeiboForm1(forms.Form):
    context = forms.CharField(widget=forms.Textarea)
def home(request, uid):
    '''显示用户和该用户发过的微薄'''
    show_user = User.objects.get(id = uid)
    weibos = show_user.get_profile().weibo.all()
    follows = show_user.get_profile().follow.all()
    users = User.objects.exclude(username__exact=request.user.username).exclude(username='root')
    show_users = []
    for var_i in xrange(3):   #随机产生最多3个
        if users:
            user = random.choice(users)
            if user not in show_users:
                if request.user.is_authenticated():
                    if user not in request.user.get_profile().follow.all(): #登录后选出不是自己已关注的人
                        show_users.append(user)
                else:
                    show_users.append(user)
    weiboform = WeiboForm1(request.POST)
    topics = Topic.objects.all()
    return render_to_response('home.html',
                {'user':show_user,
                'weibos':weibos,
                'request':request,
                'show_users':show_users,
                'topics':topics})


