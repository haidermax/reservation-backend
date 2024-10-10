from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinics.views.medical_center import MedicalCenterViewSet
from clinics.views.hospital import HospitalViewSet
from clinics.views.clinic import ClinicViewSet
from clinics.views.laboratory import LaboratoryViewSet
from clinics.views.beauty_center import BeautyCenterViewSet


router = DefaultRouter()

router.register(r'medical-centers', MedicalCenterViewSet, basename='medical_center')
router.register(r'hospitals', HospitalViewSet, basename='hospital')
router.register(r'clinics', ClinicViewSet, basename='clinic')
router.register(r'laboratories', LaboratoryViewSet, basename='laboratory')
router.register(r'beauty-centers', BeautyCenterViewSet, basename='beauty_center')

urlpatterns = [
    path('', include(router.urls)),
]