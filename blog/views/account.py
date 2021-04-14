import time
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from blog.forms.account import RegisterForm, LoginForm
from blog.models import UserInfo
from utils.cos import create_bucket



class RegisterView(View):
    """用户注册"""
    def get(self, request):

        form = RegisterForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request):

        form = RegisterForm(request.POST)

        # 校验数据--数据格式问题--密码的一致性
        if form.is_valid():
            # 保存数据
            email = form.cleaned_data['email']

            if email in settings.ADMIN_ACCOUNT:
                form.instance.is_super = True   # settings中直接设置管理员账号

                # 管理员账号需要设置存储桶
                bucket = f"PersonBlog-{email.split('@')[0]}{int(1000*time.time())}-1305490799"
                create_bucket(bucket)
                form.instance.bucket = bucket
                form.instance.region = 'ap-shanghai'
            else:
                form.instance.is_super = False  # 任何用户注册都是普通用户
            
            form.save()

            return JsonResponse({'code': 200})
        
        return JsonResponse({'code': 416, 'msg': form.errors})


class LoginView(View):
    """用户登录"""
    def get(self, request):

        form = LoginForm()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        # 校验数据--邮箱存在问题--密码的一致性
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = UserInfo.objects.filter(email=email, password=password).first()
            
            if user:
                # 用户登录成功，做session设置
                request.session['user_id'] = user.id
                request.session.set_expiry(60 * 60 * 24 * 7)

                return redirect(reverse("blog:index"))
            else:
                # 用户密码错误
                form.add_error('email', '邮箱或者密码错误')
        
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    """用户退出"""
    def get(self, request):

        request.session.flush()

        return redirect(reverse('blog:index'))
