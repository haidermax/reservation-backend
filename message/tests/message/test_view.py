from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from ...models.message import Message

class MessageCRUDTests(APITestCase):
    """
    Test suite for the Message model and viewset.
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

        # Create a test sender and receiver
        self.sender = User.objects.create_user(
            email='sender@example.com',
            full_name='Sender User',
            password='senderpassword123',
            role='patient'
        )
        self.receiver = User.objects.create_user(
            email='receiver@example.com',
            full_name='Receiver User',
            password='receiverpassword123',
            role='doctor'
        )

        # Create a sample message instance for testing
        self.message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            message_text='This is a test message.',
        )

        # URLs for message-related API actions
        self.message_list_url = reverse('message-list')
        self.message_detail_url = lambda pk: reverse('message-detail', kwargs={'pk': pk})

    def test_get_message_list(self):
        response = self.client.get(self.message_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_message_detail(self):
        response = self.client.get(self.message_detail_url(self.message.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_message(self):
        data = {
            'sender': self.sender.id,
            'receiver': self.receiver.id,
            'message_text': 'Hello, this is a new message.',
        }
        response = self.client.post(self.message_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 2)

    def test_partial_update_message(self):
        data = {'message_text': 'This is an updated message.'}
        response = self.client.patch(self.message_detail_url(self.message.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_message(self):
        response = self.client.delete(self.message_detail_url(self.message.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)