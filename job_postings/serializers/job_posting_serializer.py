from rest_framework import serializers
from job_postings.models.job_posting import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobPosting model.
    """

    class Meta:
        model = JobPosting
        fields = [
            'id',
            'service_provider',
            'service_provider_type',
            'job_title',
            'job_description',
            'qualifications',
            'salary',
            'job_location',
            'job_status',
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