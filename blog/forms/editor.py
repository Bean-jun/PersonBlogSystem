from django import forms
from blog.models import Note
from blog.forms.bootstrap import BootStrapForm


class NoteForm(BootStrapForm, forms.ModelForm):
    """note笔记表单"""

    bootstrap_class_exclude = ['top_image']

    class Meta:
        model = Note
        fields = ['title', 'content', 'top_image']
        widgets = {
            'content':forms.Textarea,
        }