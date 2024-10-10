from rest_framework import viewsets, permissions
from reservations.models.reservation import Reservation
from reservations.serializers.reservation_serializer import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting reservation instances.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the reservation with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the reservation with the user who updated it.
        """
        serializer.save(update_user=self.request.user)