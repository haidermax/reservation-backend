from rest_framework import viewsets
from clinics.models.laboratory import Laboratory
from clinics.serializers.laboratory import LaboratorySerializer

class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer