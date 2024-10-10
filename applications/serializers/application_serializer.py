from rest_framework import serializers
from applications.models.application import Application

class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Application model.
    """

    class Meta:
        model = Application
        fields = [
            'id',
            'job_seeker',
            'job',
            'resume',
            'cover_letter',
            'application_status',
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