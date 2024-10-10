from rest_framework import serializers
from ..models.message import Message

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'message_text',
            'message_image',
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]
        read_only_fields = [
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]