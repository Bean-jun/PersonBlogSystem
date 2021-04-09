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
        form = NoteForm(request.POST)

        if form.is_valid():

            form.instance.author = request.user
            form.save()

        return redirect(reverse('blog:editor'))