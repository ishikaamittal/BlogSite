from re import I
from django.shortcuts import render
from .models import PostBlog
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "home.html")

def blog_page(request):
    blogContent = {
        'posts' : PostBlog.objects.all
        }
    return render(request, "blog_page.html", blogContent)
