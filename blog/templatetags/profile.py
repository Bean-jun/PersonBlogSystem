from django.template import Library
from blog.models import UserInfo


register = Library()


@register.inclusion_tag('inclusion/user_profile.html')
def user_profile(request):
    user = UserInfo.objects.filter(id=request.user.id).first()

    return {'url': user.image}