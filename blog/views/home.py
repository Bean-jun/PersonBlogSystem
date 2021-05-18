from django.shortcuts import render
from django.views import View
from blog.models import Note, UserInfo


class IndexView(View):
    """用户中心页"""

    def get(self, request):
        notes = Note.objects.all().order_by('-create_datetime')[:14]
        user = UserInfo.objects.filter(is_super=True).first()
        context = {
            'notes': notes,
            'user': user
        }
        return render(request, 'home.html', context)


class CategoryListView(View):
    """分类列表页"""

    def get(self, request, category_id):
        """
        图片缩略图-文章标题
        """
        notes = Note.objects.filter(category_id=category_id).order_by('-create_datetime')

        return render(request, 'category_list.html', {'notes': notes})


class DetailView(View):
    """
    博客详情
    """

    def get(self, request, article_id):
        note = Note.objects.filter(id=article_id).first()

        return render(request, 'detail.html', {'note': note})
