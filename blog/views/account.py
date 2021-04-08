from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from blog.forms.account import RegisterForm, LoginForm
from blog.models import UserInfo



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
