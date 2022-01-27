from django.http import HttpResponseRedirect
from turtle import title
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from .models import PostBlog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, "home.html")

def blog_page(request):
    blogContent = {
        'posts' : PostBlog.objects.all
        }
    return render(request, "blog_page.html", blogContent)

@login_required
def addPost(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
            # post.slug =slugify(post.title)
        post.author = request.user
        post.save()
        messages.success(request,"New blog created!")
        return redirect("blog-page")
    else:
        form = PostForm(request.POST)
    return render(request,"addPost.html", {"form":form})

@login_required
def updatePost(request, id):
    method = request.method
    if method == 'GET':
        post = PostBlog.objects.filter(id=id).values().first()
        data = {'form': PostForm(post)}
        return render(request, 'addPost.html', data)
    elif method == 'POST':
        post = PostBlog.objects.get(id=id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Blog updated!")
            return redirect("blog-page")

@login_required
def deletePost(request, id):
    post = PostBlog.objects.get(id=id)
    post.delete()
    messages.success(request,"Blog deleted!")
    return redirect("blog-page")
  
