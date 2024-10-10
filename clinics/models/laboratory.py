from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User

class Laboratory(AbstractMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='laboratories', null=True, blank=True)
    laboratory_name = models.CharField(max_length=255)
    available_tests = models.TextField()
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
        return f"{self.laboratory_name} - {self.user.full_name if self.user else 'No Admin'}"