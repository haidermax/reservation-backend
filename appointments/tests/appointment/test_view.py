from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from appointments.models.appointment import Appointment

class AppointmentCRUDTests(APITestCase):
    """
    Test suite for the Appointment model and viewset.
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

        # Create a sample appointment instance for testing
        self.appointment = Appointment.objects.create(
            user=self.patient,
            service_provider_type='doctor',
            service_provider_id=1,
            appointment_date='2024-05-01',
            appointment_time='10:00',
            status='CONFIRMED',
        )

        # URLs for appointment-related API actions
        self.appointment_list_url = reverse('appointment-list')
        self.appointment_detail_url = lambda pk: reverse('appointment-detail', kwargs={'pk': pk})

    def test_get_appointment_list(self):
        response = self.client.get(self.appointment_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_appointment_detail(self):
        response = self.client.get(self.appointment_detail_url(self.appointment.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        data = {
            'user': self.patient.id,
            'service_provider_type': 'clinic',
            'service_provider_id': 2,
            'appointment_date': '2024-06-01',
            'appointment_time': '15:00',
            'status': 'PENDING',
        }
        response = self.client.post(self.appointment_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_partial_update_appointment(self):
        data = {'status': 'CANCELLED'}
        response = self.client.patch(self.appointment_detail_url(self.appointment.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment(self):
        response = self.client.delete(self.appointment_detail_url(self.appointment.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)