from rest_framework import serializers
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):
    """
    Serializer for the Reply model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Reply
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class ReplyDetailSerializer(ReplySerializer):
    """
    Additional serializer to reference the Post Id
    which the reply is associated with
    """
    post = serializers.ReadOnlyField(source='post.id')