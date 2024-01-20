from rest_framework import generics, permissions
from MewMes_API.permissions import IsOwnerOrReadOnly
from votes.models import Vote
from votes.serializers import VoteSerializer

class VoteList(generics.ListCreateAPIView):
    """
    List votes or create a vote if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a vote or owner can delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()