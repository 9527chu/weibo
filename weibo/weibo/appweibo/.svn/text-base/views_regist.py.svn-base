'''views_regist.py'''
#coding:utf8
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse , HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from weibo.appweibo.models import *
from django.contrib.auth.models import User
import re
users = User.objects.all()
def validate(value):
    for user in users:
        if value == user.username:
            raise forms.ValidationError("用户名已存在")
def validator(value):
    pp = re.compile("\w+")
    pa = pp.match(value)
    if pa is None:
        raise forms.ValidationError("密码以数字，字母，下划线组成")
class RegistForm(forms.Form):	
    '''RegistForm'''
    email = forms.EmailField(label="邮箱")
    username = forms.CharField(validators=[validate,validator],label="姓名")
    first_name = forms.CharField(max_length=30,label="昵称")
    password = forms.CharField(widget=forms.PasswordInput,label="密码")
    headimg = forms.FileField(label="头像")
def regist(request):
    '''regist'''
    if request.method == 'POST':
        registform = RegistForm(request.POST,request.FILES)
        if registform.is_valid():
            username = registform.cleaned_data['username']
            password = registform.cleaned_data['password']
            email = registform.cleaned_data['email']
            first_name = registform.cleaned_data['first_name']
            headimg = registform.cleaned_data['headimg']
            user = User.objects.create_user(
                username,
                email,
                password,
            )
            user.first_name = first_name
            user.save()
            UserProfile.objects.create(headimg=headimg, user=user)
            return HttpResponseRedirect('/index/index/')
    else:
        registform = RegistForm()
    return render_to_response('regist.html',{'registform':registform})



	

