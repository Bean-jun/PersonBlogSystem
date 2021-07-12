from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.note import NoteAPIView
from api.views.account import RegisterAPIView, LoginAPIView
from api.views.temp_token import GetToken
from api.views.machine.system import SystemInfo

app_name = 'api'

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('get_token/', GetToken.as_view()),
    path('machine/', SystemInfo.as_view()),
]

# 接口路由
router = DefaultRouter()
router.register('notes', NoteAPIView)
urlpatterns += router.urls
