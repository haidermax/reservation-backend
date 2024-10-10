from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for the service provider references

class JobPosting(AbstractMixin):
    """
    Represents a job posting created by a service provider.
    """
    JOB_STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('filled', 'Filled'),
    ]

    service_provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')  # The service provider posting the job
    service_provider_type = models.CharField(max_length=50)  # Type of service provider (e.g., doctor, hospital)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    qualifications = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional salary offered
    job_location = models.CharField(max_length=255)
    job_status = models.CharField(max_length=50, choices=JOB_STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Job Posting: {self.job_title} by {self.service_provider.full_name}"