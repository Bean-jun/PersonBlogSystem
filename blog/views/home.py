from django.shortcuts import render
from django.views import View
from blog.models import Note, UserInfo


class IndexView(View):
    """用户中心页"""
    def get(self, request):
        notes = Note.objects.all().order_by('-modify_datetime')[:14]
        user = UserInfo.objects.filter(is_super=True).first()
        context = {
            'notes': notes,
            'user': user
        }
        return render(request, 'home.html', context)


class _IndexView(View):
    """
    网站首页
    """
    def get(self, request):
        """
        图片缩略图-文章标题-摘要[正文切片]
        """
        notes = Note.objects.all().order_by('-create_datetime')

        for note in notes:
            content_cut = note.content[1:10]

            # 正文切片
            setattr(note, 'content_cut', content_cut)

        return render(request, 'index.html', {'notes': notes})


class DetailView(View):
    """
    博客详情
    """
    def get(self, request, article_id):

        note = Note.objects.filter(id=article_id).first()

        return render(request, 'detail.html', {'note': note})