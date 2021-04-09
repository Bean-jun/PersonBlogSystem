from django.shortcuts import render
from django.views import View
from blog.models import Note


class IndexView(View):
    """
    网站首页
    """
    def get(self, request):
        """
        图片缩略图-文章标题-摘要[正文切片]
        """
        notes = Note.objects.all()

        for note in notes:
            content_cut = note.content[:10]

            # 正文切片
            setattr(note, 'content_cut', content_cut)

        return render(request, 'index.html', {'notes': notes})
