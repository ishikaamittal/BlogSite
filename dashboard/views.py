from unicodedata import category
from django.shortcuts import render,HttpResponse
from Blog.models import Blog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    posts = Blog.objects.all().filter(author=user)
    content = {
        'posts': posts,
    }
    return render(request, "dashboard.html", content)


# def blog_page(request):
#     blog_list = Blog.objects.filter(status="Published")
#     page = request.GET.get('page', 1)
#     paginator = Paginator(blog_list, 5)
#     try:
#         blog_list = paginator.page(page)
#     except PageNotAnInteger:
#         blog_list = paginator.page(1)
#     except EmptyPage:
#         blog_list = paginator.page(paginator.num_pages)
#     content = {
#         'posts': blog_list,
#     }
#     return render(request, "blog_page.html", content)

@login_required
def addPost(request):
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "New blog created!")
        return redirect('blog-page')
    else:
        form = PostForm(request.POST)
    return render(request, "add_post.html", {"form": form})