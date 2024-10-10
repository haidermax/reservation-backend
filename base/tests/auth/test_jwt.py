from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class JWTAuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            full_name='Test User',
            password='testpassword123',
            role='patient'
        )
        self.token_url = reverse('token_obtain_pair')
        self.token_refresh_url = reverse('token_refresh')
        self.token_verify_url = reverse('token_verify')
        self.logout_url = reverse('custom_logout')

    def test_user_login_and_token_generation(self):
        """
        Test if the user can log in and obtain a JWT token pair (access and refresh tokens).
        """
        response = self.client.post(self.token_url, {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.access_token = response.data['access']
        self.refresh_token = response.data['refresh']

    def test_token_refresh(self):
        """
        Test refreshing an access token using a refresh token.
        """
        response = self.client.post(self.token_url, {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        
        refresh_token = response.data['refresh']
        response = self.client.post(self.token_refresh_url, {
            'refresh': refresh_token
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_user_logout_and_token_blacklisting(self):
        """
        Test logging out (blacklisting the refresh token).
        """
        response = self.client.post(self.token_url, {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        
        refresh_token = response.data['refresh']
        response = self.client.post(self.logout_url, {
            'refresh': refresh_token
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(self.token_refresh_url, {
            'refresh': refresh_token  # Use 'refresh' as the correct key here as well
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


