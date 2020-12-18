from django.urls import path
from .views import index, article, detail, edit, delete, myArticles

urlpatterns = [
    path('', index, name="index"),
    path('articles/', article, name='article'),
    path('article/<int:pk>/', detail, name='detail'),
    path('article/edit/<int:pk>/', edit, name='edit'),
    path('article/delete/<int:pk>/', delete, name='delete'),
    path('my-articles/', myArticles, name='my-articles'),
]