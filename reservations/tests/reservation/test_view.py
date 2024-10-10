from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from reservations.models.reservation import Reservation

class ReservationCRUDTests(APITestCase):
    """
    Test suite for the Reservation model and viewset.
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

        # Create a test user for the patient
        self.patient = User.objects.create_user(
            email='patient@example.com',
            full_name='Patient User',
            password='patientpassword123',
            role='patient'
        )

        # Create a sample reservation instance for testing
        self.reservation = Reservation.objects.create(
            patient=self.patient,
            service_provider_type='doctor',
            service_provider_id=1,
            appointment_date='2024-05-01',
            appointment_time='10:00',
            status='CONFIRMED',
        )

        # URLs for reservation-related API actions
        self.reservation_list_url = reverse('reservation-list')
        self.reservation_detail_url = lambda pk: reverse('reservation-detail', kwargs={'pk': pk})

    def test_get_reservation_list(self):
        response = self.client.get(self.reservation_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reservation_detail(self):
        response = self.client.get(self.reservation_detail_url(self.reservation.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_reservation(self):
        data = {
            'patient': self.patient.id,
            'service_provider_type': 'clinic',
            'service_provider_id': 2,
            'appointment_date': '2024-06-01',
            'appointment_time': '15:00',
            'status': 'PENDING',
        }
        response = self.client.post(self.reservation_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_partial_update_reservation(self):
        data = {'status': 'CANCELLED'}
        response = self.client.patch(self.reservation_detail_url(self.reservation.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reservation(self):
        response = self.client.delete(self.reservation_detail_url(self.reservation.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)