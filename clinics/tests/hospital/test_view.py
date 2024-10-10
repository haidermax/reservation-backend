from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from clinics.models.hospital import Hospital

class HospitalViewSetTests(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpassword123',
            role='admin'
        )
        self.client.login(email='admin@example.com', password='adminpassword123')

        self.instance = Hospital.objects.create(
            hospital_name='General Hospital',
            specialty='Cardiology',
            administration='Main Admin',
            bio='A brief bio for the hospital.',
            availability_time='24/7',
            gps_location='456.123, -456.123',
            advertise=True,
            phone_number='987654321'
        )
        self.list_url = reverse('hospital-list')
        self.detail_url = reverse('hospital-detail', kwargs={'pk': self.instance.pk})

    def test_get_hospital_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hospital_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['hospital_name'], 'General Hospital')

    def test_create_hospital(self):
        data = {
            'hospital_name': 'New Hospital',
            'specialty': 'Neurology',
            'administration': 'New Admin',
            'bio': 'New bio for the hospital.',
            'availability_time': '9 AM - 5 PM',
            'gps_location': '789.123, -789.123',
            'advertise': False,
            'phone_number': '123456789'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hospital.objects.count(), 2)

    def test_update_hospital(self):
        updated_data = {'hospital_name': 'Updated Hospital'}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.hospital_name, 'Updated Hospital')

    def test_delete_hospital(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hospital.objects.count(), 0)