"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from Insta.views import PostView, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, UserDetail,EditProfile

urlpatterns = [
    path('', PostView.as_view(), name = 'home'),
    path('post/<int:pk>/', PostDetail.as_view(), name = 'post_detail'),
    path('make_post/', PostCreateView.as_view(), name='make_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name = 'update_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name = 'delete_post'),
    path('user/<int:pk>/', UserDetail.as_view(), name = 'user_profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name = 'edit_profile'),
]