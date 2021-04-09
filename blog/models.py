from django.db import models


class UserInfo(models.Model):
    """用户表"""
    username = models.CharField(max_length=32, verbose_name="用户名")
    email = models.EmailField(max_length=32, verbose_name="邮箱", db_index=True)
    password = models.CharField(max_length=32, verbose_name="密码")
    is_super = models.BooleanField(default=False, verbose_name="是否为管理员")

    
class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=32, verbose_name="分类名称")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    

class Note(models.Model):
    """用户笔记表"""
    author = models.ForeignKey('UserInfo', on_delete=models.CASCADE, verbose_name="作者")
    title = models.CharField(max_length=32, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_datetime = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    top_image = models.ImageField(upload_to='note_image/', height_field='', width_field='', verbose_name="笔记快照")

  
class Image(models.Model):
    """笔记图片表"""
    note = models.ForeignKey('Note', on_delete=models.CASCADE, verbose_name='笔记')
    image = models.ImageField(upload_to='note/', verbose_name="笔记图片")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

   
class UserComment(models.Model):
    """用户评论"""
    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE, verbose_name="用户")
    note = models.ForeignKey('Note', on_delete=models.CASCADE, verbose_name="笔记")
    content = models.CharField(max_length=128, verbose_name="评论内容")
    up = models.PositiveIntegerField(verbose_name="赞")
    down = models.PositiveIntegerField(verbose_name='踩')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    is_top = models.BooleanField(default=False, verbose_name="是否置顶")

