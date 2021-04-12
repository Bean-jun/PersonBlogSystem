from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from blog.forms.editor import NoteForm


class EditorView(View):
    """图文编辑页"""
    def get(self, request):

        form = NoteForm()

        return render(request, 'editor.html', {'form': form})

    def post(self, request):
        form = NoteForm(data=request.POST, files=request.FILES)

        if form.is_valid():

            # 保存图片
            img = form.cleaned_data.get('top_image')
            file = open(img.name, 'wb')
            for data in img.chunks():
                file.write(data)
            file.close()

            form.instance.author = request.user
            form.save()

        return redirect(reverse('blog:editor'))