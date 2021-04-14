# 个人博客

----

### 零、开始内容
1.git

    git clone https://gitee.com/bean_jun/person-blog.git

2.配置文件

    2.1 django项目的settings配置

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

    2.2 uwsgi.ini的配置

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

3.nginx部分，百度下吧


### 一、基本操作
1.关闭uwsgi

    uwsgi --stop uwsgi.pid

2.搜集静态文件

    python3 manage.py collectstatic

3.启动uwsgi

    uwsgi --ini uwsgi.ini


### 二、更新小站

    重复第一大步的三个基本操作，不过需要在1，2之间来上一个git pull即可


### 三、看看小站跑起来没
