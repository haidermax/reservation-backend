from django.urls import path, include
from rest_framework.routers import DefaultRouter
from offers.views.offer_view import OfferViewSet

router = DefaultRouter()
router.register(r'offers', OfferViewSet, basename='offer')

urlpatterns = [
    path('', include(router.urls)),
]