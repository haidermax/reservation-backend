from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from job_seekers.models.job_seeker_user import JobSeekerUser

class JobSeekerUserCRUDTests(APITestCase):
    """
    Test suite for the JobSeekerUser model and viewset.
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

        # Create a test user for the job seeker
        self.user = User.objects.create_user(
            email='jobseeker@example.com',
            full_name='Job Seeker User',
            password='jobseekerpassword123',
            role='job_seeker'
        )

        # Create a test job seeker profile
        self.job_seeker = JobSeekerUser.objects.create(
            user=self.user,
            specialty='Nurse',
            degree='Bachelor of Nursing',
            address='123 Street, City',
            gps_location='123.456, -123.456'
        )

        # URLs for job seeker-related API actions
        self.job_seeker_list_url = reverse('jobseekeruser-list')
        self.job_seeker_detail_url = lambda pk: reverse('jobseekeruser-detail', kwargs={'pk': pk})

    def test_get_job_seeker_list(self):
        response = self.client.get(self.job_seeker_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_seeker_detail(self):
        response = self.client.get(self.job_seeker_detail_url(self.job_seeker.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_job_seeker(self):
        """
        Ensure we can create a new job seeker with a unique user.
        """
        # Create a new user to avoid UNIQUE constraint violation
        new_user = User.objects.create_user(
            email='newjobseeker@example.com',
            full_name='New Job Seeker User',
            password='newjobseekerpassword123',
            role='job_seeker'
        )

        # Use the new user's ID in the job seeker creation data
        data = {
            'user': new_user.id,  # Use the ID of the new user
            'specialty': 'Therapist',
            'degree': 'Master of Therapy',
            'address': '456 New Street, New City',
            'gps_location': '789.123, -789.123'
        }

        # Create the new job seeker with a unique user ID
        response = self.client.post(self.job_seeker_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobSeekerUser.objects.count(), 2)  # New job seeker should be created

    def test_partial_update_job_seeker(self):
        data = {'specialty': 'Updated Specialty'}
        response = self.client.patch(self.job_seeker_detail_url(self.job_seeker.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_job_seeker(self):
        response = self.client.delete(self.job_seeker_detail_url(self.job_seeker.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
