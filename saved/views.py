from rest_framework import generics, permissions
from MewMes_API.permissions import IsOwnerOrReadOnly
from saved.models import Saved
from saved.serializers import SavedSerializer


class SavedList(generics.ListCreateAPIView):
    """
    List saved memes or save one when logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()

    """
    Makes sure saved ones are associated with user.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavedDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and remove a saved meme by the owner only.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()
