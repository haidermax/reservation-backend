from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Import the User model for patient reference

class Reservation(AbstractMixin):
    """
    Represents a reservation made by a patient for a specific service provider.
    """
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
    ]

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')  # The patient making the reservation
    service_provider_type = models.CharField(max_length=255)  # Type of service provider (e.g., doctor, nurse)
    service_provider_id = models.IntegerField()  # Reference to the service provider's ID
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Reservation for {self.patient.full_name} on {self.appointment_date} at {self.appointment_time}"