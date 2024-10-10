from rest_framework import viewsets
from clinics.models.beauty_center import BeautyCenter
from clinics.serializers.beauty_center import BeautyCenterSerializer

class BeautyCenterViewSet(viewsets.ModelViewSet):
    queryset = BeautyCenter.objects.all()
    serializer_class = BeautyCenterSerializer