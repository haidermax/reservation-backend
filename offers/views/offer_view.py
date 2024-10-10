from rest_framework import viewsets, permissions
from offers.models.offer import Offer
from offers.serializers.offer_serializer import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting offer instances.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the offer with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the offer with the user who updated it.
        """
        serializer.save(update_user=self.request.user)