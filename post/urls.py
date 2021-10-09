from django.urls import path
from . import views
from .views import BlogPostPage

urlpatterns = [
    path('posts-categories', views.postCategory, name = 'post-category'),
    path('posts-categories/<str:post_category_url>/', views.singlePostCategory, name = 'single-post-category'),

    path('all-posts', BlogPostPage.as_view(), name= 'post'),
    path('all-posts/<str:single_post_url>/', views.singlePost, name='single-post'),
]
