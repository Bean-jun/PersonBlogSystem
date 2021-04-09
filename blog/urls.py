from django.urls import path
from blog.views import home, account

app_name = 'blog'


urlpatterns = [
    path('', home.IndexView.as_view(), name="index"), # 网站首页
    path('register/', account.RegisterView.as_view(), name='register'), # 用户注册
    path('login/', account.LoginView.as_view(), name='login'), # 用户登录
    path('logout/', account.LogoutView.as_view(), name='logout'), # 用户退出
]
