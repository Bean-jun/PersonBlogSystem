from django.shortcuts import render
from django.urls import reverse
from django.views import View
from blog.models import Note, UserInfo
from utils.pagination import Pagination
from django.core.cache import cache


class IndexView(View):
    """用户中心页"""

    def get(self, request):
        # 页面缓存，提高访问速度
        context = cache.get('index')
        if not context:
            notes = Note.objects.all().order_by('-create_datetime')[:14]
            user = UserInfo.objects.filter(is_super=True).first()
            context = {
                'notes': notes,
                'user': user
            }
            cache.set('index', context, 60 * 60 * 2)

        return render(request, 'home.html', context)


class CategoryListView(View):
    """分类列表页"""

    def get(self, request, category_id):
        """
        图片缩略图-文章标题
        """
        current_page = request.GET.get('page', 1)
        note_obj = Note.objects.filter(category_id=category_id).order_by('-create_datetime')
        note_page = Pagination(current_page=current_page,
                               per_page=12,
                               all_count=note_obj.count(),
                               base_url=request.path,
                               query_params=request.GET,
                               pager_page_count=5)

        notes = note_obj[note_page.start:note_page.end]

        context = {'notes': notes,
                   'count': note_obj.count(),
                   'page_html': note_page.page_html()}

        return render(request, 'category_list.html', context)
