from django import  forms
from blog.models import Note
from blog.forms.bootstrap import BootStrapForm


class NoteForm(BootStrapForm, forms.ModelForm):
    """note笔记表单"""

    class Meta:
        model = Note
        fields = ['title', 'content']