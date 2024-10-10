from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from job_postings.models.job_posting import JobPosting
from applications.models.application import Application

class ApplicationCRUDTests(APITestCase):
    """
    Test suite for the Application model and viewset.
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
            job_title='Data Analyst',
            job_description='Data analyst with 2+ years of experience.',
            qualifications='Bachelor in Data Science',
            salary=6000,
            job_location='Office B',
            job_status='open',
        )

        # Create a sample application instance for testing
        self.application = Application.objects.create(
            job_seeker=self.job_seeker,
            job=self.job_posting,
            resume='Sample resume text.',
            cover_letter='Sample cover letter text.',
            application_status='submitted',
        )

        # URLs for application-related API actions
        self.application_list_url = reverse('application-list')
        self.application_detail_url = lambda pk: reverse('application-detail', kwargs={'pk': pk})

    def test_get_application_list(self):
        response = self.client.get(self.application_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_application_detail(self):
        response = self.client.get(self.application_detail_url(self.application.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_application(self):
        data = {
            'job_seeker': self.job_seeker.id,
            'job': self.job_posting.id,
            'resume': 'New resume text.',
            'cover_letter': 'New cover letter text.',
            'application_status': 'submitted',
        }
        response = self.client.post(self.application_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 2)

    def test_partial_update_application(self):
        data = {'application_status': 'reviewed'}
        response = self.client.patch(self.application_detail_url(self.application.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_application(self):
        response = self.client.delete(self.application_detail_url(self.application.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)