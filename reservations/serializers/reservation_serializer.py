from rest_framework import serializers
from reservations.models.reservation import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reservation model.
    """

    class Meta:
        model = Reservation
        fields = [
            'id',
            'patient',
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