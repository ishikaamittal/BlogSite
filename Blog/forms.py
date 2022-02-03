from tkinter import Widget
from django import forms
from .models import PostBlog


class PostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ["title","content","category"]

    CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ANDROID', 'Android'),
        ('PC', 'PC'),
        ('GAMING', 'Gaming'),
        ('OTHERS', 'Others'),
    ]
    title= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Article content', 'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))

class updatePostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ["title","content","category"]
