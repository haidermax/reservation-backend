from rest_framework import serializers
from clinics.models.medical_center import MedicalCenter

class MedicalCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCenter
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'create_user', 'update_user', 'is_archived']