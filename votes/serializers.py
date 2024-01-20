from rest_framework import serializers
from votes.models import Vote

class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vote model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = ['id', 'created_at', 'owner', 'post']