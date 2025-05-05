from rest_framework import generics, permissions
from django.core.cache import cache
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user = self.request.user
        cache_key = f'article_list_{user.id if user.is_authenticated else "anon"}'
        cached_qs = cache.get(cache_key)
        if cached_qs:
            return cached_qs

        queryset = Article.objects.all()
        cache.set(cache_key, queryset, 60)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
