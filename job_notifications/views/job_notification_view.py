from rest_framework import viewsets, permissions
from job_notifications.models.job_notification import JobNotification
from job_notifications.serializers.job_notification_serializer import JobNotificationSerializer

class JobNotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting job notification instances.
    """
    queryset = JobNotification.objects.all()
    serializer_class = JobNotificationSerializer
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