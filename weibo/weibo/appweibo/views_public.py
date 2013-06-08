#-*- coding:utf8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django import forms
import models
import re

def weibo_add(request):
    """ 发布微博 """
    if request.method == "POST":
        context = request.POST.get('context', '')
        if context:
            topic_context = re.findall(r'(#.+#)', context)
            if topic_context:       #是否有话题
                topic_length = len(topic_context[0])
                context = context[topic_length:]
                title = topic_context[0].strip('##') #去掉两边的‘##’
                topics = models.Topic.objects.filter(title__exact=title) #查看是否已存在话题
                if not topics:
                    topic = models.Topic.objects.create(title=title, user=request.user) 
            weibo = models.Weibo(context=context)
            weibo.save()
            if topic_context:
                if not topics:
                    topic.weibo.add(weibo)  #添加微博到新建话题
                else:
                    topics[0].weibo.add(weibo)  #添加微博到已有话题
            request.user.userprofile.weibo.add(weibo)
            x =  request.user.userprofile.weibo.all()[0]
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) # 发布微博成功后，返回到提交前的页面
        else:
            return HttpResponse('微博为空，请发布有效的微博')
    else:
        return HttpResponse('不是一个POST提交')

def ulogin(request):
    ''' 登录'''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username and password:
            user = auth.authenticate(username=username,password=password)
            print user
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/myhome/myhome/')
                    # 发布微博成功后，返回到提交前的页面
            return HttpResponse('用户认证失败')
        else:
            return HttpResponse('用户名或密码为空')
    else:
        return HttpResponse('不是一个POST提交')
def ulogout(request):
    '''注销'''
    auth.logout(request)
    return HttpResponseRedirect('/index/index/')
    

class ReplyForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea, required=False)
    
def weibo_reply(request, uid):
    '''评论'''
    weibo = models.Weibo.objects.get(id=uid)
    replys = weibo.reply.all()
    replyform = ReplyForm(request.POST)
    return render_to_response('reply.html', {'weibo': weibo, 'replys': replys, 'replyform': replyform, 'request': request})

def weibo_reply_add(request, uid):
    '''发评论'''
    weibo = models.Weibo.objects.get(id=uid)
    if request.method == 'POST':
        context = request.POST.get('context')
        if context:
            reply = models.Reply.objects.create(context=context, user = request.user)
            weibo.reply.add(reply)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) # 发布评论成功后，返回到提交前的页面
        else:
            return HttpResponse('评论为空，请发布有效的微博')
    else:
        return HttpResponse('不是一个POST提交')
def collect_add(request, uid):
    '''收藏'''
    weibo = models.Weibo.objects.get(id=uid)
    request.user.get_profile().collect.add(weibo)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) # 收藏成功后，返回到提交前的页面

def collect(request):
    '''收藏页面'''
    collects = request.user.get_profile().collect.all()
    return render_to_response('collect.html', {'collects': collects, 'request': request})

def forwarding(request, uid):
    weibo = models.Weibo.objects.get(id=uid)
    replyform = ReplyForm(request.POST)
    return render_to_response('forwarding.html', {'replyform': replyform, 'weibo': weibo, 'request': request})    
def forwarding_add(request, uid):
    weibo = models.Weibo.objects.get(id=uid)
    if request.method == 'POST':
        context = request.POST.get('context')
        if context:
            reply = models.Reply.objects.create(context=context, user=request.user)
            weibo.reply.add(reply)
            newweibo = models.Weibo.objects.create(context=context, forwarding=weibo)
            request.user.get_profile().weibo.add(newweibo)
            return HttpResponseRedirect('/myhome/myhome/') # 发布微博成功后，返回到主页
        else:
            return HttpResponse('微博为空，请发布有效的微博')
    else:
        return HttpResponse('不是一个POST提交')
def follow_add(request, uid):
    '''增加关注'''
    user = User.objects.get(id=uid)
    request.user.get_profile().follow.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) # 关注成功后，返回到提交前的页面
    
