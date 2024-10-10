from rest_framework import serializers
from clinics.models.laboratory import Laboratory

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'create_user', 'update_user', 'is_archived']