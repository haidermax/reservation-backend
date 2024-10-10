from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for creator and updater fields

class Offer(AbstractMixin):
    """
    Represents a special offer provided by a service provider (e.g., doctor, hospital, clinic).
    """
    SERVICE_PROVIDER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('laboratory', 'Laboratory'),
        ('beauty_center', 'Beauty Center'),
        ('pharmacist', 'Pharmacist'),
    ]

    service_provider_id = models.IntegerField()  # Reference to the service provider's ID
    service_provider_type = models.CharField(max_length=50, choices=SERVICE_PROVIDER_TYPE_CHOICES)
    offer_title = models.CharField(max_length=255)
    offer_description = models.TextField()
    offer_image = models.CharField(max_length=255, null=True, blank=True)  # Optional image URL
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    period_of_time = models.CharField(max_length=255)  # Duration of the offer (e.g., "1 week")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.offer_title} ({self.service_provider_type})"