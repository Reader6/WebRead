from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from . import models
from . import forms
from .models import User
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())    #locals返回当前所有的本地变量字典
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            # head_img=register_form.cleaned_data.get('img_head')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    # register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录则返回登录页
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

def user(request):

    if request.method == 'GET':
        id = request.session['user_id']
        user_name = request.session['user_name']


        images = User.objects
        images = images.filter(name=user_name)
        return render(request, 'login/user.html', {'images': images,'id':id,'user_name':user_name,})
    if request.method == 'POST':
        icon = request.FILES.get('img')
        email=request.POST.get('email')
        sex=request.POST.get("ss")
        nn=request.POST.get('nn')

        user_name = request.session['user_name']
        # User.objects.creat(head_img=icon)
        models.User.objects.filter(name=user_name).update(head_img=icon)
        models.User.objects.filter(name=user_name).update(email=email)
        models.User.objects.filter(name=user_name).update(sex=sex)

        # 将图片保存在media文件中，且存储的是相对路径
        # obj=models.User.objects.get(name=user_name)
        # obj.head_img=icon
        # obj.save()

        return HttpResponse('上传成功')
        # return render(request, 'login/user.html')


    # img = get_object_or_404(User,id);



    # login_form = forms.UserForm(request.POST)
    # username = login_form.cleaned_data.get('username')
    # user = models.User.objects.get(name=username);
    # return render(request, 'login/user.html',{'id':id,'user_name':user_name,'img':img})


