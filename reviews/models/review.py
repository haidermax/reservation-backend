from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for the reviewer reference

class Review(AbstractMixin):
    """
    Represents a review left by a user for a service provider.
    """
    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # The user leaving the review
    service_provider_type = models.CharField(max_length=255)  # Type of service provider (e.g., doctor, nurse)
    service_provider_id = models.IntegerField()  # Reference to the service provider's ID
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user.full_name} - Rating: {self.rating}"