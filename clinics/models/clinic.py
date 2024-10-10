from django.db import models
from base.models.abstract_mixin import AbstractMixin
from doctors.models import Doctor
from .medical_center import MedicalCenter

class Clinic(AbstractMixin):
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.SET_NULL, related_name='clinics', null=True, blank=True)
    clinic_name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, related_name='clinics', null=True, blank=True)
    working_hours = models.CharField(max_length=255)
    gps_location = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.clinic_name} - {self.doctor.user.full_name if self.doctor else 'No Doctor Assigned'}"