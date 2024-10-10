from rest_framework import serializers
from job_notifications.models.job_notification import JobNotification

class JobNotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobNotification model.
    """

    class Meta:
        model = JobNotification
        fields = [
            'id',
            'job',
            'job_seeker',
            'notification_text',
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