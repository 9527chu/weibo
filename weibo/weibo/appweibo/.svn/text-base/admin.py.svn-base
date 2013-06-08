##-*- coding: utf-8 -*-
#
from django.contrib import admin
from django.contrib.auth.models import User, Group
from weibo.appweibo.models import *

admin.site.unregister(User) #卸载user admin，并重新注册
admin.site.register(User,UserProfileAdmin)
admin.site.register(Weibo)
admin.site.register(Reply)
admin.site.register(Topic)
