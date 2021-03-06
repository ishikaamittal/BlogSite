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
from dashboard import views as dash_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='blog-home'),
    # dashboard
    path('dashboard/', dash_views.dashboard, name='dashboard'),
    path('favorite/<id>',dash_views.favorite_add, name="favorite_add"),
    path('favorites/',dash_views.favorites, name="favorites"),
    # blog
    path('blogs/', blog_views.blog_page, name='blog-page'),
    path('category/<str:category>', blog_views.category_wise, name='category-page'),
    path('addpost/', dash_views.addBlog, name="add-post"),
    path('update/<id>', blog_views.updateBlog, name="update-post"),
    path('delete/<id>', blog_views.deleteBlog, name="delete-post"),
    path('article/<id>',blog_views.article, name="article"),
    

    # user
    path('register/', users_views.Register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/Login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/Logout.html'), name='logout' ),
        # password reset
    path("password_reset", users_views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/reset_password_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/reset_password_complete.html'), name='password_reset_complete'),      
#    syntax has asterik * for static files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
