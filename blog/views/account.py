from django.shortcuts import render
from django.views import View
from blog.forms.account import RegisterForm, LoginForm



class RegisterView(View):
    """用户注册"""
    def get(self, request):

        form = RegisterForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request):
        pass


class LoginView(View):
    """用户登录"""
    def get(self, request):

        form = LoginForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request):
        pass