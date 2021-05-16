from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from api.views import NoteAPIView

app_name = 'api'

urlpatterns = [
]

# 接口路由
router = DefaultRouter()
router.register('notes', NoteAPIView)
urlpatterns += router.urls
