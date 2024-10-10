from rest_framework import viewsets, permissions
from ..models.message import Message
from ..serializers.message_serializer import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting message instances.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the message with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the message with the user who updated it.
        """
        serializer.save(update_user=self.request.user)