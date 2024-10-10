from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from job_postings.models.job_posting import JobPosting

class JobPostingCRUDTests(APITestCase):
    """
    Test suite for the JobPosting model and viewset.
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

        # Create a test service provider
        self.provider = User.objects.create_user(
            email='provider@example.com',
            full_name='Service Provider',
            password='providerpassword123',
            role='doctor'
        )

        # Create a sample job posting instance for testing
        self.job_posting = JobPosting.objects.create(
            service_provider=self.provider,
            service_provider_type='hospital',
            job_title='Nurse',
            job_description='Nurse with experience in ER.',
            qualifications='Bachelor in Nursing',
            salary=5000,
            job_location='Hospital A',
            job_status='open',
        )

        # URLs for job posting-related API actions
        self.job_posting_list_url = reverse('jobposting-list')
        self.job_posting_detail_url = lambda pk: reverse('jobposting-detail', kwargs={'pk': pk})

    def test_get_job_posting_list(self):
        response = self.client.get(self.job_posting_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_posting_detail(self):
        response = self.client.get(self.job_posting_detail_url(self.job_posting.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_job_posting(self):
        data = {
            'service_provider': self.provider.id,
            'service_provider_type': 'clinic',
            'job_title': 'Medical Assistant',
            'job_description': 'Assist doctors with patients.',
            'qualifications': 'Certificate in Medical Assistance',
            'salary': 3000,
            'job_location': 'Clinic B',
            'job_status': 'open',
        }
        response = self.client.post(self.job_posting_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPosting.objects.count(), 2)

    def test_partial_update_job_posting(self):
        data = {'job_title': 'Senior Nurse'}
        response = self.client.patch(self.job_posting_detail_url(self.job_posting.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_job_posting(self):
        response = self.client.delete(self.job_posting_detail_url(self.job_posting.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)