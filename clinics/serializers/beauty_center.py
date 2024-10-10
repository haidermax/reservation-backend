from rest_framework import serializers
from clinics.models.beauty_center import BeautyCenter

class BeautyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyCenter
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'create_user', 'update_user', 'is_archived']