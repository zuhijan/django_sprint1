from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
]
