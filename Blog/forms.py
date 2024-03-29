# from tkinter import Widget
from django import forms
from .models import Blog

CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('TECHNOLOGY', 'Technology'),
        ('GAMES', 'Games'),
        ('MARKETING/SALES','Marketing/Sales'),
        ('OTHERS', 'Others'),
    ]

STATUS_CHOICES = [
    ('Draft', 'Draft'),
    ('Published', 'Published')
]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content","category","image","status","favorites"]

   
    title= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':25, 'cols':15, 'placeholder': 'Article content', 'class': 'form-control'}))
    category = forms.ChoiceField(label='Category',choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))
    status = forms.ChoiceField(label='Status',choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))

class updateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content","category","image","status"]
    title= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Article content', 'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))
    status = forms.ChoiceField(label='Status',choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))


