from django.db import models
from base.models.abstract_mixin import AbstractMixin  # Import the AbstractMixin from base app
from base.models.user import User  # Import the custom User model for foreign key relationships

class Doctor(AbstractMixin):
    """
    Doctor model representing the doctor profile with additional fields.
    Inherits common fields from AbstractMixin.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    medical_center_id = models.IntegerField(null=True, blank=True)  # Placeholder, assume it references another model in future
    specialty = models.CharField(max_length=255)
    degrees = models.CharField(max_length=255)
    bio = models.TextField()
    address = models.CharField(max_length=255, null=True, blank=True)
    availability_time = models.CharField(max_length=255)  # e.g., "9 AM - 5 PM"
    advertise = models.BooleanField(default=False)  # Indicates if the doctor paid for advertising
    advertise_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    advertise_duration = models.CharField(max_length=50, null=True, blank=True)  # 'month' or 'year'
    is_international = models.BooleanField(default=False)
    country = models.CharField(max_length=255, null=True, blank=True)

    # Fields like profile_image and phone_number are handled in the User model
    # Use `user.profile_image` and `user.phone_number` for reference

    def __str__(self):
        return f"{self.user.full_name} - {self.specialty}"
