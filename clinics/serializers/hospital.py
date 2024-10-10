from rest_framework import serializers
from clinics.models.hospital import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'create_user', 'update_user', 'is_archived']