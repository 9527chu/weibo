#coding:utf8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from weibo.appweibo.models import *
import os.path
import random
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
def follow_show(request, uid):
    if request.user.is_authenticated():
    
        user = User.objects.get(id=uid)
        weibo_number = len(user.userprofile.weibo.all())
        follow = user.userprofile.follow.all()
        users = User.objects.exclude(username__exact=request.user.username).exclude(username='root')
        '''
        imgname = user.get_profile().headimg.name
        for img in imgname:
            img = user.get_profile().headimg.name
            imgname = os.path.basename(img)
            user.imgname = imgname
        '''
 
        for user in users:
            weibo_num = user.get_profile().weibo.all()
            user.weibo_num = len(weibo_num)
            headimg = user.get_profile().headimg.name
            headimg = os.path.basename(headimg)
            user.headimg = headimg

        show_users = []
        for var_i in xrange(3):   #随机产生最多3个
            user = random.choice(users)
            if user not in show_users:
                if request.user.is_authenticated():
                    if user not in request.user.get_profile().follow.all(): #登录后选出不是自己已关注的人
                        show_users.append(user)
                else:
                    show_users.append(user)

        topics = Topic.objects.all()
        follows = user.userprofile.follow.all()
        p = Paginator(follows,4)
        page=request.GET.get('page')
        try:
            contacts = p.page(page)
        except PageNotAnInteger:
            contacts = p.page(1)
        except EmptyPage:
            contacts = p.page(p.num_pages)
        
        return render_to_response('follow.html',{'follow':follow,'contacts':contacts,'request':request,'weibo_number':weibo_number, 'show_users': show_users, 'topics': topics,'headimg':headimg})
    else:
        return HttpResponse("请先<a href='/index/index/'>/登录/</a>")
