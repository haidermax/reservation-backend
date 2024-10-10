from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from reviews.models.review import Review

class ReviewCRUDTests(APITestCase):
    """
    Test suite for the Review model and viewset.
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

        # Create a test user for the review
        self.reviewer = User.objects.create_user(
            email='reviewer@example.com',
            full_name='Reviewer User',
            password='reviewerpassword123',
            role='patient'
        )

        # Create a sample review instance for testing
        self.review = Review.objects.create(
            user=self.reviewer,
            service_provider_type='doctor',
            service_provider_id=1,
            rating=5,
            review_text='Excellent service and very professional.',
        )

        # URLs for review-related API actions
        self.review_list_url = reverse('review-list')
        self.review_detail_url = lambda pk: reverse('review-detail', kwargs={'pk': pk})

    def test_get_review_list(self):
        response = self.client.get(self.review_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_detail(self):
        response = self.client.get(self.review_detail_url(self.review.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        data = {
            'user': self.reviewer.id,
            'service_provider_type': 'clinic',
            'service_provider_id': 2,
            'rating': 4,
            'review_text': 'Very good service.',
        }
        response = self.client.post(self.review_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

    def test_partial_update_review(self):
        data = {'rating': 2}
        response = self.client.patch(self.review_detail_url(self.review.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_review(self):
        response = self.client.delete(self.review_detail_url(self.review.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)