from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from blog.forms.editor import NoteForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from blog.models import Note
from utils.cos import upload_file


class EditorView(View):
    """图文编辑页"""
    def get(self, request):

        form = NoteForm()

        return render(request, 'editor.html', {'form': form})

    def post(self, request):
        form = NoteForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            image_obj = form.cleaned_data['top_image']

            # 首页图片回传到cos
            # 上传图片
            url = upload_file(bucket=request.user.bucket,
                              image_obj=image_obj,
                              region=request.user.region)

            # 返回数据
            form.instance.top_image = url
            form.instance.author = request.user
            form.save()

            return redirect(reverse('blog:article', args=(form.instance.id,)))

        return render(request, 'editor.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class ImageUploadView(View):
    def post(self, request):
        context = {
            # 上传成功success为1，url为上传成功后的返回链接，用于图片显示，message用于提示
            "success": 0,
            "message": None,
            "url": None
        }
        # 图片内容
        image_obj = request.FILES.get('editormd-image-file')

        if not image_obj:
            context['message'] = '文件不存在'
            return JsonResponse(context)

        # 上传图片
        context['url'] = upload_file(bucket=request.user.bucket,
                                     image_obj=image_obj,
                                     region=request.user.region)

        # 返回数据
        context['success'] = 1

        return JsonResponse(context)


class ModifyView(View):
    """图文修改页"""
    def get(self, request, note_id):

        note = Note.objects.filter(id=note_id).first()
        if not note:
            return redirect(reverse('blog:editor'))

        form = NoteForm(initial=dict(title=note.title, content=note.content))

        return render(request, 'editor.html', {'form': form})

    def post(self, request, note_id):
        note = Note.objects.get(id=note_id)

        form = NoteForm(instance=note, data=request.POST, files=request.FILES)

        if form.is_valid():
            image_obj = form.cleaned_data['top_image']
            if not image_obj.name.startswith('https://personblog'):
                # 表示用户需要重新上传图片文件
                url = upload_file(bucket=request.user.bucket,
                                  image_obj=image_obj,
                                  region=request.user.region)
                form.instance.top_image = url

            # 返回数据
            form.save()
            return redirect(reverse('blog:article', args=(form.instance.id,)))

        return render(request, 'editor.html', {'form': form})