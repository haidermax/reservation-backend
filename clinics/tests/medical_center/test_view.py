from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from clinics.models.medical_center import MedicalCenter

class MedicalCenterViewSetTests(APITestCase):

    def setUp(self):
        # Create a superuser for authentication
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpassword123',
            role='admin'
        )
        self.client.login(email='admin@example.com', password='adminpassword123')

        # Create a sample MedicalCenter instance for testing
        self.instance = MedicalCenter.objects.create(
            center_name='Sample Medical Center',
            director_name='Dr. John Doe',
            bio='A brief bio for the medical center.',
            availability_time='9 AM - 5 PM',
            gps_location='123.456, -123.456',
            advertise=True,
            phone_number='123456789'
        )

        # URLs for MedicalCenter API actions
        self.list_url = reverse('medical_center-list')
        self.detail_url = reverse('medical_center-detail', kwargs={'pk': self.instance.pk})

    def test_get_medical_center_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_medical_center_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['center_name'], 'Sample Medical Center')

    def test_create_medical_center(self):
        data = {
            'center_name': 'New Medical Center',
            'director_name': 'Dr. Jane Doe',
            'bio': 'New bio for the medical center.',
            'availability_time': '10 AM - 6 PM',
            'gps_location': '789.123, -789.123',
            'advertise': False,
            'phone_number': '987654321'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicalCenter.objects.count(), 2)

    def test_update_medical_center(self):
        updated_data = {'center_name': 'Updated Medical Center'}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.center_name, 'Updated Medical Center')

    def test_delete_medical_center(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MedicalCenter.objects.count(), 0)