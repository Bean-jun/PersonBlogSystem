from datetime import datetime, timedelta

from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from apps.api.models import VisitorRecord
from apps.blog.models import UserInfo
from apps.oauth.models import UserInfoWeiBo


class Tracer:
    """封装user和price_policy的数据，便于视图函数访问"""

    def __init__(self):
        self.user = None
        self.price_policy = None
        self.project = None  # 将项目进行封装


class LoginMiddleware(MiddlewareMixin):
    """校验用户是否登录"""

    def process_request(self, request):

        request.tracer = Tracer()

        REMOTE_ADDR = request.META.get("REMOTE_ADDR")
        REMOTE_HOST = request.META.get("REMOTE_HOST")
        VisitorRecord.objects.create(addr=REMOTE_ADDR, host=REMOTE_HOST)

        # 匿名用户
        user = None

        user_id, flag = request.session.get('user_id', [0, 0])

        if flag == "origin":
            # 注册用户
            user = UserInfo.objects.filter(id=user_id).first()

        elif flag == 'weibo':
            # 微博授权用户
            user = UserInfo.objects.filter(username=user_id).first()
            user_info_access = UserInfoWeiBo.objects.filter(user_id=user.id).first()
            today = datetime.now()
            # 验证过期需要重新登录
            if timedelta(seconds=int(user_info_access.expires)) + user_info_access.modify_datetime < today:
                user = None

        # 将获取到的用户放置在request中
        request.user = user
        request.tracer.user = user

    def process_view(self, request, view, args, kwargs):
        """非管理员或者未登录用户，只能看白名单页面"""
        try:
            if (request.user is None) or (request.user.email not in settings.ADMIN_ACCOUNT):
                if not request.path.split('/')[1] in settings.VISITOR_WHITE_FUNCTION:
                    return redirect(reverse('blog:index'))
        except Exception as e:
            raise Http404
