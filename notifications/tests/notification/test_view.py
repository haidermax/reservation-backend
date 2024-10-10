from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from notifications.models.notification import Notification

class NotificationCRUDTests(APITestCase):
    """
    Test suite for the Notification model and viewset.
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

        # Create a test user for the notification recipient
        self.user = User.objects.create_user(
            email='recipient@example.com',
            full_name='Recipient User',
            password='recipientpassword123',
            role='patient'
        )

        # Create a sample notification instance for testing
        self.notification = Notification.objects.create(
            user=self.user,
            notification_text='Your appointment is scheduled for tomorrow.',
            is_read=False
        )

        # URLs for notification-related API actions
        self.notification_list_url = reverse('notification-list')
        self.notification_detail_url = lambda pk: reverse('notification-detail', kwargs={'pk': pk})

    def test_get_notification_list(self):
        response = self.client.get(self.notification_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notification_detail(self):
        response = self.client.get(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_notification(self):
        data = {
            'user': self.user.id,  # Use the user ID reference for foreign key
            'notification_text': 'Your test results are ready.',
            'is_read': False
        }
        response = self.client.post(self.notification_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notification.objects.count(), 2)

    def test_partial_update_notification(self):
        data = {'is_read': True}
        response = self.client.patch(self.notification_detail_url(self.notification.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_notification(self):
        response = self.client.delete(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)