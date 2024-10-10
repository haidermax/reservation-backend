from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CustomLoginView(TokenObtainPairView):
    """
    Custom login view if you want to add additional logic during login.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'access': response.data.get('access'),
            'refresh': response.data.get('refresh'),
        }, status=status.HTTP_200_OK)
