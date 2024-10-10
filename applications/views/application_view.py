from rest_framework import viewsets, permissions
from applications.models.application import Application
from applications.serializers.application_serializer import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting application instances.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the application with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the application with the user who updated it.
        """
        serializer.save(update_user=self.request.user)