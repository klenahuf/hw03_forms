from django.forms import ModelForm

from .models import Post


class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
