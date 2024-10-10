from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for job seeker reference
from job_postings.models.job_posting import JobPosting  # Assuming JobPosting is used for job reference

class JobNotification(AbstractMixin):
    """
    Represents a job notification sent to a job seeker related to a specific job posting.
    """
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='notifications')  # The job related to the notification
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_notifications')  # The job seeker receiving the notification
    notification_text = models.TextField()  # Text of the notification

    def __str__(self):
        return f"Notification for {self.job_seeker.full_name} - Job: {self.job.job_title}"