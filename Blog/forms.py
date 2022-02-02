from tkinter import Widget
from django import forms
from .models import PostBlog


class PostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ["title","content","category"]

    title= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Article content', 'class': 'form-control'}))
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'category', 'class': 'form-control'}))

class updatePostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ["title","content","category"]
