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

# def Register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')
#             return redirect('blogs/')
#     else:
#         form = UserRegisterForm()
#     return render(request, "register.html", {'form': form})
