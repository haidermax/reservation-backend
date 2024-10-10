from rest_framework import viewsets, permissions
from ..models import Doctor
from ..serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Assign different permissions based on the action.
        Only admin users can delete doctors, others can list, retrieve, and update.
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        if self.action in ['update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Save the doctor with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the doctor with the user who updated it.
        """
        serializer.save(update_user=self.request.user)
