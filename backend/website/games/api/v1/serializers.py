from rest_framework import serializers

from games.models import DrinkingGame


class DrinkingGameSerializer(serializers.ModelSerializer):
    """Drinking Game serializer."""

    class Meta:
        """Meta class."""

        model = DrinkingGame
        fields = ["name", "description", "items"]
