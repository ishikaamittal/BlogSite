from unicodedata import category
from django.shortcuts import render,HttpResponse
from .models import PostBlog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, updatePostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, "home.html")


def blog_page(request):
    blog_list = PostBlog.objects.all()
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
def addPost(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "New blog created!")
        return redirect('blog-page')
    else:
        form = PostForm(request.POST)
    return render(request, "add_post.html", {"form": form})

def article(request, id):
    article = PostBlog.objects.filter(id=id).first()
    return render(request, "article.html" ,{"article": article})

def category_wise(request, category):
    articles = PostBlog.objects.filter(category=category.upper())
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
def updatePost(request,id):
    instance = PostBlog.objects.filter(id=id).first()
    # if user is the author of the article
    if request.user == instance.author:
        if request.method == 'POST':
            form = updatePostForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('blog-page')
        else:
            form = updatePostForm(instance=instance)
    return render(request, 'update_post.html', {'form': form})


@login_required
def deletePost(request, id):
    post = PostBlog.objects.get(id=id)
    if request.user == post.author:
        post.delete()
        messages.success(request, "Blog deleted!")
        return redirect("blog-page")
