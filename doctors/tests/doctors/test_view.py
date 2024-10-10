from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from base.models.user import User
from doctors.models import Doctor

class DoctorCRUDTests(APITestCase):
    def setUp(self):
        # Create a superuser for authentication
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpassword123',
            role='admin'
        )

        # Log in as the superuser
        self.client.login(email='admin@example.com', password='adminpassword123')

        # URLs for doctor-related API actions
        self.doctor_list_url = reverse('doctor-list')
        self.doctor_detail_url = lambda pk: reverse('doctor-detail', kwargs={'pk': pk})

        # Create a test user for the doctor
        self.user = User.objects.create_user(
            email='doctor@example.com',
            full_name='Doctor User',
            password='doctorpassword123',
            role='doctor',
            phone_number='123456789',
        )

        # Create a test doctor
        self.doctor = Doctor.objects.create(
            user=self.user,
            specialty='Cardiology',
            degrees='MBBS, MD',
            bio='Experienced cardiologist with 10 years of practice.',
            address='123 Street, City',
            availability_time='9 AM - 5 PM',
            is_international=False,
            country='Country Name',
            advertise=False,
        )

    def test_create_doctor(self):
        """
        Ensure we can create a new doctor using the user UUID.
        """
        # Create a new user for the doctor
        new_user = User.objects.create_user(
            email='newdoctor@example.com',
            full_name='New Doctor',
            password='newdoctorpassword123',
            role='doctor',
            phone_number='987654321'
        )

        data = {
            'user': str(new_user.id),  # Pass the UUID of the user
            'specialty': 'Neurology',
            'degrees': 'MBBS, MD',
            'bio': 'Neurologist with 8 years of experience.',
            'address': '456 New Street, New City',
            'availability_time': '10 AM - 6 PM',
            'is_international': True,
            'country': 'New Country',
            'advertise': True,
            'advertise_price': '1000.00',
            'advertise_duration': 'year',
        }

        response = self.client.post(self.doctor_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)

        # Ensure the doctor was created with the correct user and specialty
        doctor = Doctor.objects.get(user=new_user)
        self.assertEqual(doctor.specialty, 'Neurology')
        self.assertEqual(doctor.user.email, 'newdoctor@example.com')

    def test_get_doctor_list(self):
        """
        Ensure we can retrieve the list of doctors.
        """
        response = self.client.get(self.doctor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Doctor.objects.count())

    def test_get_doctor_detail(self):
        """
        Ensure we can retrieve a specific doctor by ID.
        """
        response = self.client.get(self.doctor_detail_url(self.doctor.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_doctor(self):
        """
        Ensure we can partially update a doctor's details.
        """
        data = {'specialty': 'Partially Updated Specialty'}

        response = self.client.patch(self.doctor_detail_url(self.doctor.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.specialty, 'Partially Updated Specialty')

    def test_delete_doctor(self):
        """
        Ensure we can delete a doctor (admin only).
        """
        response = self.client.delete(self.doctor_detail_url(self.doctor.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctor.objects.count(), 0)

    def test_archived_state(self):
        """
        Ensure the doctor can be archived (set `is_archived` to True).
        """
        # Set the doctor to archived
        self.doctor.is_archived = True
        self.doctor.save()

        # Fetch the doctor again
        response = self.client.get(self.doctor_detail_url(self.doctor.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_archived'])

        # Verify in the database
        self.doctor.refresh_from_db()
        self.assertTrue(self.doctor.is_archived)
