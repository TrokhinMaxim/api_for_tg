from rest_framework import serializers
from .models import CurrencyRequest

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class CurrencySerializer(serializers.Serializer):
    exchange_rate = serializers.FloatField()
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    def create(self, validated_data):
        return CurrencyRequest.objects.create(**validated_data)


class CurrencyRequestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRequest
        fields = ["exchange_rate", "date"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["active_follow"]


class GreetingSerializer(serializers.Serializer):
    user_username = serializers.CharField()


class CurrencyTemplateSerializer(serializers.Serializer):
    exchange_rate = serializers.FloatField()
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")


class UserHistoryTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRequest
        fields = ["exchange_rate", "date"]
