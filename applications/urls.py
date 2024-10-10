from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.views.application_view import ApplicationViewSet

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]