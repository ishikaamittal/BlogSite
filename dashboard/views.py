from unicodedata import category
from django.shortcuts import render,HttpResponse
from Blog.models import Blog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    posts = Blog.objects.filter(author=user)
    data = {}
    data['user'] = user
    data['posts'] = posts
    return render(request, "index.html", data)
