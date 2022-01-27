from django.shortcuts import render
from .models import PostBlog
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
def index(request):
    return render(request, "home.html")

def blog_page(request, page=1):

        # pagination

    # page = request.GET.get('page', 1)
    blog_list = PostBlog.objects.all()
    paginator = Paginator(blog_list, 4)

    try:
        blog_list = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        blog_list = paginator.page(paginator.num_pages)
            

    content = {
        'posts' : blog_list,
        }
    return render(request, "blog_page.html",content)

@login_required
def addPost(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
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
  
