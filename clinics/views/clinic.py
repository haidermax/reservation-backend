from rest_framework import viewsets
from clinics.models.clinic import Clinic
from clinics.serializers.clinic import ClinicSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer