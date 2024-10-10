from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from job_postings.models.job_posting import JobPosting
from job_notifications.models.job_notification import JobNotification

class JobNotificationCRUDTests(APITestCase):
    """
    Test suite for the JobNotification model and viewset.
    """

    def setUp(self):
        # Create a superuser for authentication
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpassword123',
            role='admin'
        )
        self.client.login(email='admin@example.com', password='adminpassword123')

        # Create a test job seeker and job posting
        self.job_seeker = User.objects.create_user(
            email='jobseeker@example.com',
            full_name='Job Seeker User',
            password='jobseekerpassword123',
            role='job_seeker'
        )

        self.job_posting = JobPosting.objects.create(
            service_provider=self.superuser,
            service_provider_type='hospital',
            job_title='Nurse',
            job_description='Looking for experienced nurse.',
            qualifications='Nursing Degree',
            salary=4000,
            job_location='Hospital A',
            job_status='open',
        )

        # Create a sample notification instance for testing
        self.notification = JobNotification.objects.create(
            job=self.job_posting,
            job_seeker=self.job_seeker,
            notification_text='A new nurse position has been posted.',
        )

        # URLs for job notification-related API actions
        self.notification_list_url = reverse('jobnotification-list')
        self.notification_detail_url = lambda pk: reverse('jobnotification-detail', kwargs={'pk': pk})

    def test_get_notification_list(self):
        response = self.client.get(self.notification_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notification_detail(self):
        response = self.client.get(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_notification(self):
        data = {
            'job': self.job_posting.id,
            'job_seeker': self.job_seeker.id,
            'notification_text': 'This is a new job notification.',
        }
        response = self.client.post(self.notification_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobNotification.objects.count(), 2)

    def test_partial_update_notification(self):
        data = {'notification_text': 'Updated notification text.'}
        response = self.client.patch(self.notification_detail_url(self.notification.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_notification(self):
        response = self.client.delete(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)