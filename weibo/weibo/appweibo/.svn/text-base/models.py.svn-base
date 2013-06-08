#-*- coding:utf-8 -*-
#!/usr/bin/env python

import datetime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# 扩展User
class UserProfile(models.Model):
    user  = models.OneToOneField(User)       # 用户登陆验证表
    weibo = models.ManyToManyField('Weibo', verbose_name=u"发微",  null=True, blank=True)
    follow = models.ManyToManyField(User, verbose_name=u"关注", related_name='milestone_task', null=True, blank=True)
    collect = models.ManyToManyField('Weibo', verbose_name=u"收藏", related_name='milestone_task', null=True, blank=True)
    headimg = models.FileField(u'头像', upload_to="./")

    class Meta:
        verbose_name = u"配置"
        verbose_name_plural = u"用户配置"
    def __unicode__(self):
        return self.user.username

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline,] # 为User的Admin界面扩展内容
    list_display = ['username', 'id',  'email', 'first_name', 'last_login', 'is_active']


class Weibo(models.Model):
    """ 微博类 """
    reply = models.ManyToManyField('Reply', verbose_name=u"评论")
    forwarding = models.ForeignKey('Weibo', verbose_name=u"转发", null=True, blank=True)
    context = models.TextField(u'内容')     # 内容
    p_time  = models.DateTimeField(auto_now=True)   # 时间
    class Meta:
        ordering = ['-p_time']

class Reply(models.Model):
    user = models.ForeignKey(User, verbose_name=u"评论者")
    context = models.TextField(u'内容')     # 内容
    p_time  = models.DateTimeField(auto_now=True)   # 时间

class Topic(models.Model):
    user = models.ForeignKey(User, verbose_name=u"话题发起人")
    weibo = models.ManyToManyField('Weibo', verbose_name=u"话题微博")

    title = models.CharField(u'标题', max_length=200)     # 标题
    p_time  = models.DateTimeField(auto_now=True)   # 时间

