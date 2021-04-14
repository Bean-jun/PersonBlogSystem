from django import forms
from blog.models import Note
from blog.forms.bootstrap import BootStrapForm


class NoteForm(BootStrapForm, forms.ModelForm):
    """note笔记表单"""
    title = forms.CharField(label='',
                            required=True,
                            min_length=1,
                            max_length=32,
                            error_messages={
                                'min_length': '标题不要太短',
                                'max_length': '标题不要太长',
                                'required': '不可以是空的哦'
                            })

    content = forms.CharField(label='',
                              required=True,
                              min_length=5,
                              error_messages={
                                 'min_length': '内容不要太短',
                                 'required': '不可以是空的哦'
                              },
                              widget=forms.Textarea)


    bootstrap_class_exclude = ['top_image']

    class Meta:
        model = Note
        fields = ['title', 'content', 'top_image']
