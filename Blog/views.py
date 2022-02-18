from email import message
from multiprocessing.sharedctypes import Value
from turtle import up
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,HttpResponse
from .models import Blog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, updateBlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    posts = Blog.objects.order_by('-views')[:4]
    return render(request, "home.html", {'posts': posts})


def blog_page(request):
    blog_list = Blog.objects.filter(status="Published")
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 5)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    content = {
        'posts': blog_list,
    }
    return render(request, "blog_page.html", content)

@login_required
def article(request, id):
    article = Blog.objects.filter(id=id).first()
    article.views = article.views + 1
    article.save()
    if article.favorites.filter(id=request.user).exists():
        fav = True
    return render(request, "article.html" ,{"article": article,'user': request.user,"fav":fav})

def category_wise(request, category):
    articles = Blog.objects.filter(category=category.upper())
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)    
    return render(request, "category_page.html" ,{"articles": articles, "category":category})

@login_required
def updateBlog(request,id):
    instance = Blog.objects.filter(id=id).first()
    # if user is the author of the article
    if request.user == instance.author:
        if request.method == 'POST':
            form = updateBlogForm(request.POST,request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('blog-page')
        else:
            form = updateBlogForm(instance=instance)
    return render(request, 'update_post.html', {'form': form})


@login_required
def deleteBlog(request, id):
    post = Blog.objects.get(id=id)
    if request.user == post.author:
        post.delete()
        messages.success(request, "Blog deleted!")
        return redirect("dashboard")
