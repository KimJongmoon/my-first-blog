from __future__ import unicode_literals
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'image', 'text', )
