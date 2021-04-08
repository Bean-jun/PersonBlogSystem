from django import forms
from django.forms import ValidationError
from blog.models import UserInfo
from utils.encrypt import md5


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
                               error_messages={
                                   'min_length': '密码不易太短',
                                   'max_length': '密码不易太长',
                               },
                               widget=forms.PasswordInput())
    
    confirm_password = forms.CharField(label='重复密码',
                                       min_length=8,
                                       max_length=32,
                                       error_messages={
                                            'min_length': '密码不易太短',
                                            'max_length': '密码不易太长',
                                        },
                                       widget=forms.PasswordInput())

    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'password']

    def clean_email(self):
        """校验邮箱"""
        email = self.cleaned_data['email']

        exists = UserInfo.objects.filter(email=email).exists()
        if exists:
            raise ValidationError("该邮箱已注册")
        
        return email

    def clean_password(self):
        """加密密码"""
        password = self.cleaned_data['password']
        
        return md5(password)

    def clean_confirm_password(self):
        """校验密码"""
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']

        if md5(confirm_password) != password:
            raise ValidationError("两次密码不一致")

        return confirm_password


class LoginForm(BootStrapForm, forms.ModelForm):
    """用户登录校验"""

    password = forms.CharField(label='密码',
                               min_length=8,
                               max_length=32,
                               error_messages={
                                   'min_length': '密码不易太短',
                                   'max_length': '密码不易太长',
                               },
                               widget=forms.PasswordInput())
    class Meta:
        model = UserInfo
        fields = ['email', 'password']

    def clean_email(self):
        """校验邮箱"""
        email = self.cleaned_data['email']

        exists = UserInfo.objects.filter(email=email).exists()
        if not exists:
            raise ValidationError("该邮箱未注册")
        
        return email

    def clean_password(self):
        """加密密码"""
        password = self.cleaned_data['password']
        
        return md5(password)