from rest_framework import serializers
from reviews.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'service_provider_type',
            'service_provider_id',
            'rating',
            'review_text',
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