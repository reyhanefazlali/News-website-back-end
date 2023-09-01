from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.sidebar_blog,name='blog'),
    path('blogdetails/<int:num>/',views.blog_details,name='blog_details'),
    path('category/<str:cat>/',views.index,name='category'),
    path('elements/',views.elements,name='elements'),
    path('lastestnews/',views.lastest_news,name='lastest_news'),
    path('author/<str:auth>/',views.index,name='author'),
    path('search/',views.search_news,name='search'),
    path('tags/<str:tag>',views.index,name='tag_cloud'),
]


