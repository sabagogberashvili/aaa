from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreatView(generics.ListCreateAPIView):
    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

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
        elif self.request.method == ['DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    

