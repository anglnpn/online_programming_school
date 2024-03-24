from rest_framework import serializers

from payments.models import Payments, Subscribe


class PaymentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для платежей
    """

    class Meta:
        model = Payments
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подписки
    """

    class Meta:
        model = Subscribe
        fields = '__all__'
