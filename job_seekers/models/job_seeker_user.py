from django.db import models
from base.models.abstract_mixin import AbstractMixin  # Import the abstract mixin for common fields
from base.models.user import User  # Import the custom User model for foreign key relationships

class JobSeekerUser(AbstractMixin):
    """
    Represents a job seeker user profile with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    specialty = models.CharField(max_length=255)  # Specialty or field of expertise
    degree = models.CharField(max_length=255)  # Degree or qualifications
    degree_image = models.CharField(max_length=255, null=True, blank=True)  # Image of the degree certificate
    address = models.CharField(max_length=255, null=True, blank=True)
    gps_location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.specialty}"