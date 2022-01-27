from django import forms
from .models import PostBlog


class PostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ["title","content","category"]
