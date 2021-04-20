from django.urls import path
from blog.views import home, account, editor

app_name = 'blog'


urlpatterns = [
    # 网站首页及详细页
    path('', home.IndexView.as_view(), name="index"), # 网站首页
    path('detail/<int:article_id>/', home.DetailView.as_view(), name="article"), # 笔记详情

    # 账户注册登录部分
    path('register/', account.RegisterView.as_view(), name='register'), # 用户注册
    path('login/', account.LoginView.as_view(), name='login'), # 用户登录
    path('logout/', account.LogoutView.as_view(), name='logout'), # 用户退出
    path('profile/', account.ProFileView.as_view(), name='profile'), # 用户个人中心

    # 文章编辑页
    path('editor/', editor.EditorView.as_view(), name='editor'), # 用户编辑
    path('modify/<int:note_id>/', editor.ModifyView.as_view(), name='modify'), # 用户修改
    path('editor/image_upload/', editor.ImageUploadView.as_view(), name="image_upload"),  # 图片上传
]
