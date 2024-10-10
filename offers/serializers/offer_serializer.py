from rest_framework import serializers
from offers.models.offer import Offer

class OfferSerializer(serializers.ModelSerializer):
    """
    Serializer for the Offer model.
    """

    class Meta:
        model = Offer
        fields = [
            'id',
            'service_provider_id',
            'service_provider_type',
            'offer_title',
            'offer_description',
            'offer_image',
            'discount_percentage',
            'original_price',
            'discounted_price',
            'period_of_time',
            'start_date',
            'end_date',
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