"""BlogSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from Blog import views as blog_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='blog-home'),
    path('blogs/<int:page>', blog_views.blog_page, name='blog-page'),
    path('register/', users_views.Register, name='register'),
    path('profile/', users_views.Profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/Login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/Logout.html'), name='logout' ),
    path('addpost/', blog_views.addPost, name="add-post"),
    path('update/<id>', blog_views.updatePost, name="update-post"),
    path('delete/<id>', blog_views.deletePost, name="delete-post"),
#    syntax has asterik * for static files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
