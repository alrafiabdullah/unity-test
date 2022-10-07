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

    def validate_email(self, value):
        try:
            EmailSubscription.objects.get(email=value)
            return value
        except:
            raise serializers.ValidationError("Email not found")

    def create(self, validated_data):
        return super().create(validated_data)
