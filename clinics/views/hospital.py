from rest_framework import viewsets
from clinics.models.hospital import Hospital
from clinics.serializers.hospital import HospitalSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer