from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.views import TokenBlacklistView


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

    path('', include(router.urls)),
        # JWT login (token generation)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT token refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Verify token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
]
