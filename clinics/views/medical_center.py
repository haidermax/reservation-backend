from rest_framework import viewsets
from clinics.models.medical_center import MedicalCenter
from clinics.serializers.medical_center import MedicalCenterSerializer

class MedicalCenterViewSet(viewsets.ModelViewSet):
    queryset = MedicalCenter.objects.all()
    serializer_class = MedicalCenterSerializer