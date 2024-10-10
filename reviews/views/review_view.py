from rest_framework import viewsets, permissions
from reviews.models.review import Review
from reviews.serializers.review_serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting review instances.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the review with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the review with the user who updated it.
        """
        serializer.save(update_user=self.request.user)