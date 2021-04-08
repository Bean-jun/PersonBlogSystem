from django import forms
from blog.models import UserInfo


class BootStrapForm(object):
    """创建Bootstrap样式"""
    def __init__(self, *args, **kwargs):
        super(BootStrapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = "请输入{}".format(field.label)


class RegisterForm(BootStrapForm, forms.ModelForm):
    """用户注册校验"""

    password = forms.CharField(label='密码',
                               min_length=8,
                               max_length=32,
                               widget=forms.PasswordInput())
    
    confirm_password = forms.CharField(label='重复密码',
                                       min_length=8,
                                       max_length=32,
                                       widget=forms.PasswordInput())

    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'password']


class LoginForm(BootStrapForm, forms.ModelForm):
    """用户登录校验"""
    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'password']