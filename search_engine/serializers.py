from rest_framework import serializers

from search_engine.models import Text


class TextSerializer(serializers.ModelSerializer):
    """
    Сериализатор для текста
    """

    class Meta:
        model = Text
        fields = '__all__'


