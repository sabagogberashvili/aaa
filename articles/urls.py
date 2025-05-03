from django.urls import path
from .views import ArticleListCreatView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListCreatView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]