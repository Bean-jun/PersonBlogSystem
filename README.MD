# 个人博客

**重要更新：**

**该项目的Flask版本正在制作中，欢迎大家发issues！**

**初版blog功能上线啦**

**地址:```https://github.com/Bean-jun/PersonBlogSystemFlask.git```**

**消息提前放送：这个django版本的我会打tag，后面会将SimpleSaaS集成到这里面来哦~**

## 一、 食用指南

### 0. 开始内容

- 0.1 git clone 项目

    ```shell
    git clone https://github.com/Bean-jun/PersonBlogSystem.git
    ```

- 0.2 配置文件

    ```shell
    0.2.1 django项目的settings配置
    
    这部分直接放在setup.py文件最佳，方便后期直接更新blog
        # 安全秘钥
        SECRET_KEY = 'xxx'
    
        # 调试模式及全站访问
        DEBUG = False
        ALLOWED_HOSTS = ['*']
    
        # 用于静态文件收集
        # python manage.py collectstatic
        STATIC_ROOT = 'xxx'
    
        # 管理员账号
        ADMIN_ACCOUNT = ['xxx']
    
        # 腾讯云对象存储
        TENCENT_SECRET_ID = 'xxx'
        TENCENT_SECRET_KEY = 'xxx'
    
        # 访客注册账号存储桶
        TENCENT_BUCKET = 'PersonBlog-visitor-1305490799'
        TENCENT_REGION = 'ap-shanghai'
    
        # 语雀账户Token - 供同步语雀平台数据使用
        YUQUE_TOKEN = "xxxxxxx"
        
        # 配置缓存
        CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/1",
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }
        
        # 配置session存储到缓存中
        SESSION_ENGINE = "django.contrib.sessions.backends.cache"
        SESSION_CACHE_ALIAS = "default"
    
    0.2.2 uwsgi.ini的配置
    
    这部分直接放在uwsgi.ini中即可,其中chdir，check-static，static-map和STATIC_ROOT保持一致即可
        [uwsgi]
        #使用nginx连接时使用
        socket=127.0.0.1:8080
        #项目目录
        chdir='xxx'
        #项目中wsgi.py文件的目录，相对于项目目录
        wsgi-file=PersonBlog/wsgi.py
        processes=2
        threads=1
        master=True
        pidfile=uwsgi.pid
        daemonize=uwsgi.log
        module = PersonBlog.wsgi:application
        # 用于检查静态文件目录
        check-static = 'xxx'
        # =前面的/static是uWSGI的URL前缀，而后面的/srv/django/static则是静态文件的路径。 这个路径，通常使用绝对路径，但也支持相对路径。
        static-map = 'xxx'
    ```

- 0.3 nginx部分，百度下吧

### 1. 基本操作

- 1.1 关闭uwsgi

    ```shell
    uwsgi --stop uwsgi.pid
    ```

- 1.2 搜集静态文件

    ```shell
    python3 manage.py collectstatic
    ```

- 1.3 启动uwsgi

    ```shell
    uwsgi --ini uwsgi.ini
    ```

### 2. 更新小站

    重复第一大步的三个基本操作，不过需要在1，2之间来上一个git pull即可

### 3. 看看小站跑起来没

    有问题欢迎发issues


## 二、 开发进度

### 1. 账号权限

账号权限部分分为管理员、普通用户及访客，其各自的权限和职能如下

- 通用权限【管理员、普通用户、访客】
    - 首页访问 √
    - 分类博客列表访问 √
    - 博客详细页访问 √

- 管理员
    - 账号注册和登录 √
    - 修改头像 √
    - 修改密码 √
    - 查看个人主页 √
    - 添加文章 √
    - 修改文章 √
    - 评论文章 √

- 普通用户
    - 账号注册和登录 √
    - 修改头像 √
    - 修改密码 √
    - 查看个人主页【显示用户评论信息】 √
    - 评论文章 √

### 2. 博客主页

- 显示管理员个人信息 √
- 管理员最近14篇博客文章 √

### 3. 博客列表页

- 通过头部导航栏进入到相关分类的博客列表页 √
- 列表页实现分页处理 √
- 列表页使用Markdown进行渲染处理 √

### 4. 博客详细页

- 管理员可以针对当前博客文章进行内容修改及文章的评论 √
- 普通用户可以进行评论 √

### 5. 个人主页

- 普通用户显示个人信息及评论 √
- 管理员用户显示个人信息及评论 √
- 管理员添加主页音乐权限 √
- 管理员其他接口集成 √

### 6. 通用接口

- 机器数据上传及下载 √
