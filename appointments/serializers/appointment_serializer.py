from rest_framework import serializers
from appointments.models.appointment import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Appointment model.
    """

    class Meta:
        model = Appointment
        fields = [
            'id',
            'user',
            'service_provider_type',
            'service_provider_id',
            'appointment_date',
            'appointment_time',
            'status',
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