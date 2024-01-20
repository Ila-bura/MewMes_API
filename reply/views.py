from rest_framework import generics, permissions
from MewMes_API.permissions import IsOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer

class ReplyList(generics.ListCreateAPIView):
    """
    List replies or create a reply when logged in.
    """
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reply.objects.all()

    """
    Makes sure replies are associated with user upon creation.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, retrieve and delete a reply by the owner only.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyDetailSerializer
    queryset = Reply.objects.all()