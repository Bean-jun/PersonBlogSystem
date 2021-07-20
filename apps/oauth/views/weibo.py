import requests
from django.conf import settings
from django.shortcuts import redirect
from django.views import View

from apps.blog.models import UserInfo
from apps.oauth.models import UserInfoWeiBo


class WeiboLogin(View):
    """获取授权页面"""

    def get(self, request):
        weibo_login = f"https://api.weibo.com/oauth2/authorize?" \
                      f"client_id={settings.WEIBO_CLIENT_ID}&" \
                      f"redirect_uri={settings.WEIBO_CALL_BACK_URL}"

        return redirect(weibo_login)


class WeiboOAuthView(View):
    """微博用户授权"""

    def get(self, request):
        code = request.GET.get('code', None)

        if not code:
            return redirect('oauth:weibo_login')

        # 获取用户token
        base_url = "https://api.weibo.com/oauth2/access_token"
        data = {
            "client_id": settings.WEIBO_CLIENT_ID,
            "client_secret": settings.WEIBO_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": settings.WEIBO_CALL_BACK_URL,
            "code": code
        }

        response = requests.post(base_url, data)

        if response.status_code == 200:
            data = response.json()

            try:
                user = UserInfo.objects.get(username=data['uid'])
            except UserInfo.DoesNotExist:
                # 保存用户信息
                user = UserInfo.objects.create(username=data['uid'],
                                               bucket=settings.TENCENT_BUCKET,
                                               region=settings.TENCENT_REGION)

                UserInfoWeiBo.objects.create(user=user,
                                             access_token=data['access_token'],
                                             expires=data['expires_in'])
            else:
                # 处理用户token
                user_weibo = UserInfoWeiBo.objects.filter(user=user).first()
                user_weibo.access_token = data['access_token']
                user_weibo.expires = data['expires_in']
                user_weibo.save()

            request.session['user_id'] = [data['uid'], 'weibo']

            return redirect('blog:profile')
        else:
            return redirect('oauth:weibo_login')
