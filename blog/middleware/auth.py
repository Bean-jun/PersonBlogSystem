from django.utils.deprecation import MiddlewareMixin
from blog.models import UserInfo


class LoginMiddleware(MiddlewareMixin):
    """校验用户是否登录"""
    def process_request(self, request):
        user_id = request.session.get('user_id', 0)

        user = UserInfo.objects.filter(id=user_id).first()

        # 将获取到的用户放置在request中
        request.user = user