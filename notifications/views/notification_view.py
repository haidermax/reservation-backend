from rest_framework import viewsets, permissions
from notifications.models.notification import Notification
from notifications.serializers.notification_serializer import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting notification instances.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the notification with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the notification with the user who updated it.
        """
        serializer.save(update_user=self.request.user)