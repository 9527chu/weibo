'''views_search '''
#coding:utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from weibo.appweibo import models  
from django import forms
import os, random
class SForm(forms.Form): 
    '''表单 ''' 
    name = forms.CharField(label = '', required = False)       
def search_person(request):
    topics = models.Topic.objects.all()
    users = User.objects.exclude(username=request.user.
        username).exclude(username='root')
    show_users = []
    # while len(show_users) < 2:  #随机产生2个用户，推荐收听
    for var_i in xrange(3):   #随机产生最多3个
        user = random.choice(users)
        if user not in show_users:
            if request.user.is_authenticated(): 
                #登录后选出不是自己已关注的人
                if user not in request.user.get_profile().follow.all(): 
                    show_users.append(user)
            else:
                show_users.append(user)
     
    part_users=[]
    for num in xrange(50):
        user = random.choice(users)
        if user not in part_users:
            if request.user.is_authenticated(): 
                #登录后选出不是自己已关注的人
                if user not in request.user.get_profile().follow.all(): 
                    part_users.append(user)
            else:
                part_users.append(user)
    if request.method == 'POST':
        searchform = SForm(request.POST)
        if searchform.is_valid():
            name = searchform.cleaned_data['name']
            userss = User.objects.exclude(username='root').filter(first_name__icontains
                = name).order_by('-id')
            usersss = User.objects.exclude(username='root').filter(username__icontains 
                = name).order_by('-id')
            return render_to_response('search.html',{'searchform':searchform, 
                'users':users, 'userss':userss, 'usersss':usersss, \
                'topics':topics, 'request':request, 'show_users':show_users})
    else:
        searchform = SForm()
    return render_to_response('search.html',{'searchform':searchform, 
        'request':request, 'users':users, 'topics':topics, 
        'show_users':show_users, 'part_users':part_users})
class WForm(forms.Form): 
    word = forms.CharField(label = '',required = False)       
def search_word(request):
    topics = models.Topic.objects.all()
    weiboss = models.Weibo.objects.all()
    users = User.objects.exclude(username=request.user.username).exclude(
        username='root')
    show_users = []
    # while len(show_users) < 2:  #随机产生2个用户，推荐收听
    for var_i in xrange(3):   #随机产生最多3个
        user = random.choice(users)
        if user not in show_users:
            if request.user.is_authenticated():
                #登录后选出不是自己已关注的人
                if user not in request.user.get_profile(
                    ).follow.all(): 
                    show_users.append(user)
            else:
                show_users.append(user)
    part_weibos=[]
    for num in xrange(50):
        weibo = random.choice(weiboss)
        if weibo not in part_weibos:
            if request.user.is_authenticated(): 
                #登录后选出不是自己已关注的人
                if weibo not in request.user.get_profile().weibo.all(): 
                    part_weibos.append(weibo)
            else:
                part_weibos.append(weibo)

    if request.method == 'POST':
        searchform = WForm(request.POST)
        if searchform.is_valid():
            word = searchform.cleaned_data['word']
            weibos = models.Weibo.objects.filter(context__icontains=word
               ).order_by('-id')
            return render_to_response('search.html',{'searchform':searchform, 
                'weibos':weibos, 'request':request, 'users':users, 
                'topics':topics, 'show_users':show_users})
    else:
        searchform = WForm()
    return render_to_response('search.html',{'searchform':searchform, 
        'request':request, 'users':users, 
        'topics':topics, 'show_users':show_users, 'weiboss':weiboss, 'part_weibos':part_weibos})
        

       
