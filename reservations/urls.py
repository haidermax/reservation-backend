from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservations.views.reservation_view import ReservationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]