from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for patient reference

class Appointment(AbstractMixin):
    """
    Represents a confirmed appointment for a patient with a specific service provider.
    """
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')  # The patient making the appointment
    service_provider_type = models.CharField(max_length=255)  # Type of service provider (e.g., doctor, nurse)
    service_provider_id = models.IntegerField()  # Reference to the service provider's ID
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Appointment for {self.user.full_name} on {self.appointment_date} at {self.appointment_time}"