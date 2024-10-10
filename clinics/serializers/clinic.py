from rest_framework import serializers
from clinics.models.clinic import Clinic

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'create_user', 'update_user', 'is_archived']