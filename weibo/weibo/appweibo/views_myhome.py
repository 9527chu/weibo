#coding:utf8
'''views'''
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django import forms
from weibo.appweibo.models import *
import random
import os
class WeiboForm(forms.Form):
    context = forms.CharField(widget = forms.Textarea, required=False, label='')
def myhome(request):
    '''xianshi'''   
    if request.user.is_authenticated():

        user = request.user
        my_weibos = user.get_profile().weibo.all()
        follows = user.get_profile().follow.all()
        show_all_user = list(follows)
        show_all_user.append(user)
        weibo_lib_time = []
        weibo_lib = []
        for x_user in show_all_user:
            for x_weibo in x_user.get_profile().weibo.all():
                weibo_lib_time.append(x_weibo.p_time)
        weibo_lib_time.sort(reverse=True)
        for time in weibo_lib_time:
            weibos = Weibo.objects.filter(p_time=time)
            if weibos:
                for weibo in weibos:
             #  if weibo.userprofile_set.all()[0].user in show_all_user:
                   weibo_lib.append(weibo)

    # while len(show_users) < 2:  #随机产生2个用户，推荐收听
        users = User.objects.exclude(username__exact=request.user.username).exclude(username='root')
        show_users = []
        for var_i in xrange(3):   #随机产生最多3个
            user = random.choice(users)
            if user not in show_users:
                if request.user.is_authenticated():
                    if user not in request.user.get_profile().follow.all(): #登录后选出不是自己已关注的人
                        show_users.append(user)
                else:
                    show_users.append(user)

        weiboform = WeiboForm(request.POST)
        topics = Topic.objects.all()
        for user in follows:
            imgname = user.get_profile().headimg.name
            print imgname
            imgname = os.path.basename(imgname)
            user.imgname = imgname

        return render_to_response('myhome.html',{'follows':follows, 'weibo_lib': weibo_lib, 'weiboform': weiboform, 'request': request, 'show_all_user': show_all_user, 'show_users': show_users, 'topics': topics})
    else:
        return HttpResponse("请先<a href = '/index/index/'>/登录/</a>")
'''
def myhome1(request , uid):
    user = User.objects.get(id = uid)
    if request.method == 'POST':
        userform = WeiboForm(request.POST)
        if userform.is_valid():
            content = userform.cleaned_data['content']
            Weibo.objects.create(content = content , user = request.user)
            return HttpResponseRedirect('/myhome.html/%s'%uid)
    else:
            userform = WeiboForm()
    return render_to_response('myhome.html' , {'userform':userform})
class ReplyForm(forms.Form):
    content = forms.CharField(widget = forms.Textarea)
def myhome2(request , uid):
    weibo = Weibo.objects.get(id=uid)
    if request.method == 'POST':
        reweibo = ReplyForm(request.POST)
        if reweibo.is_valid():
            content = reweibo.cleaned_data['content']
            Reply.objects.create(content=content,weibo=weibo,user=request.user)
            return HttpResponseRedirect('/myhome.html/')
    else:                    
        reweibo=ReplyForm()  
    return render_to_response('myhome.html',{'reweibo':reweibo})
'''    
