from rest_framework import generics, permissions
from MewMes_API.permissions import IsOwnerOrReadOnly
from downvotes.models import DownVote
from downvotes.serializers import DownVoteSerializer


class DownVoteList(generics.ListCreateAPIView):
    """
    List downvotes or create a downvote if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DownVoteSerializer
    queryset = DownVote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DownVoteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a downvote or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DownVoteSerializer
    queryset = DownVote.objects.all()
