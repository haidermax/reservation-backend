from rest_framework import viewsets, permissions
from appointments.models.appointment import Appointment
from appointments.serializers.appointment_serializer import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting appointment instances.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the appointment with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the appointment with the user who updated it.
        """
        serializer.save(update_user=self.request.user)