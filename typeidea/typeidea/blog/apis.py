from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post, Category, Tag
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]    # used for POST, PUT, DELETE, no need for this GET only class

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    """
    # seializers.py, class CategoryDetailSerializer(CategorySerializer):
    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    """

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)

"""
# api_view(['GET', 'POST']）
@api_view()
def post_list(request):
    posts = Post.objects.filter(status=Post.STATUS_NORMAL)
    post_serializers = PostSerializer(posts, many=True)
    return Response(post_serializers.data)
"""

"""
class PostList(generics.ListAPIView):       # GET supported
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer
"""

"""
class PostList(generics.ListCreateAPIView): # GET, POST supported
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer
"""