from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from offers.models.offer import Offer

class OfferCRUDTests(APITestCase):
    """
    Test suite for the Offer model and viewset.
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

        # Create a sample offer instance for testing
        self.offer = Offer.objects.create(
            service_provider_id=1,
            service_provider_type='doctor',
            offer_title='50% Off for New Patients',
            offer_description='Get 50% off your first consultation.',
            discount_percentage=50.00,
            original_price=200.00,
            discounted_price=100.00,
            period_of_time='1 month',
            start_date='2024-01-01T00:00:00Z',
            end_date='2024-02-01T00:00:00Z',
        )

        # URLs for offer-related API actions
        self.offer_list_url = reverse('offer-list')
        self.offer_detail_url = lambda pk: reverse('offer-detail', kwargs={'pk': pk})

    def test_get_offer_list(self):
        response = self.client.get(self.offer_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_offer_detail(self):
        response = self.client.get(self.offer_detail_url(self.offer.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_offer(self):
        data = {
            'service_provider_id': 2,
            'service_provider_type': 'clinic',
            'offer_title': '25% Discount on All Services',
            'offer_description': 'Get 25% discount on all health services for a limited time.',
            'discount_percentage': 25.00,
            'original_price': 100.00,
            'discounted_price': 75.00,
            'period_of_time': '2 weeks',
            'start_date': '2024-03-01T00:00:00Z',
            'end_date': '2024-03-15T00:00:00Z',
        }
        response = self.client.post(self.offer_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_partial_update_offer(self):
        data = {'offer_title': 'Updated Offer Title'}
        response = self.client.patch(self.offer_detail_url(self.offer.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_offer(self):
        response = self.client.delete(self.offer_detail_url(self.offer.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)