from rest_framework import serializers
from ..models import Doctor
from base.models.user import User  # Import your User model

class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Doctor model.
    """
    user = serializers.UUIDField(format='hex_verbose')  # Accept user UUID as a string

    class Meta:
        model = Doctor
        fields = [
            'id',
            'user',  # User now accepts UUID as a string
            'specialty',
            'degrees',
            'bio',
            'address',
            'availability_time',
            'advertise',
            'advertise_price',
            'advertise_duration',
            'is_international',
            'country',
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]
        read_only_fields = [
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]

    def create(self, validated_data):
        """
        Create a new doctor profile.
        """
        user_uuid = validated_data.pop('user')
        user = User.objects.get(id=user_uuid)  # Fetch the user by UUID
        doctor = Doctor.objects.create(user=user, **validated_data)  # Create doctor
        return doctor

    def update(self, instance, validated_data):
        """
        Update an existing doctor profile.
        """
        user_uuid = validated_data.pop('user', None)
        if user_uuid:
            instance.user = User.objects.get(id=user_uuid)
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
