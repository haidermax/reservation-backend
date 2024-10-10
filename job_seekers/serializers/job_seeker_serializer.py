from rest_framework import serializers
from job_seekers.models.job_seeker_user import JobSeekerUser
from base.models.user import User  # Import the User model
class JobSeekerUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobSeekerUser model.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Use the primary key related field

    class Meta:
        model = JobSeekerUser
        fields = [
            'id',
            'user',
            'specialty',
            'degree',
            'degree_image',
            'address',
            'gps_location',
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
