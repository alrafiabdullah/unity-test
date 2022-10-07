from rest_framework import serializers

from .models import EmailSubscription


class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = "__all__"


class EmailSubscriptionCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
        required = ("email",)

    def create(self, validated_data):
        return super().create(validated_data)
