from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'role',
            'profile_image',
            'gps_location',
            'phone_number',
            'is_active',
            'is_staff',
            'is_superuser',
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
        
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
        }

    def create(self, validated_data):
        """Create a new user with an encrypted password."""
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Encrypt the password
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update an existing user and handle password encryption."""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Encrypt the password if provided
        instance.save()
        return instance
