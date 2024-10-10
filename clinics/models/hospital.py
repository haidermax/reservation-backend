from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User

class Hospital(AbstractMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='hospitals', null=True, blank=True)
    hospital_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    administration = models.CharField(max_length=255)
    bio = models.TextField()
    address = models.CharField(max_length=255, null=True, blank=True)
    availability_time = models.CharField(max_length=255)
    gps_location = models.CharField(max_length=255, null=True, blank=True)
    advertise = models.BooleanField(default=False)
    advertise_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    advertise_duration = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.hospital_name} - {self.specialty}"