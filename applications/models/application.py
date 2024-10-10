from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for job seekers reference
from job_postings.models.job_posting import JobPosting  # Assuming JobPosting is used for job reference

class Application(AbstractMixin):
    """
    Represents a job application submitted by a job seeker for a specific job posting.
    """
    APPLICATION_STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')  # Job seeker applying for the job
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')  # The job the user is applying for
    resume = models.TextField(null=True, blank=True)  # Optional resume (could be a link to a file or plain text)
    cover_letter = models.TextField(null=True, blank=True)  # Optional cover letter
    application_status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f"Application by {self.job_seeker.full_name} for {self.job.job_title}"