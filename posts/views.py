from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from MewMes_API.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        downvotes_count=Count('downvotes', distinct=True),
        reply_count=Count('replies', distinct=True),
        saved_count=Count('saved', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # user feed
        'owner__followed__owner__profile',
        # user saved posts
        'saved__owner__profile',
        # user posts
        'owner__profile',
    ]
    ordering_fields = [
        'votes_count',
        'downvotes_count'
        'reply_count',
        'votes__created_at',
        'downvotes__created_at',
        'saved_count',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        downvotes_count=Count('downvotes', distinct=True),
        reply_count=Count('replies', distinct=True),
        saved_count=Count('saved', distinct=True),
    ).order_by('-created_at')
