from rest_framework.generics import ListAPIView, RetrieveAPIView

from games.api.v1.serializers import DrinkingGameSerializer
from games.models import DrinkingGame


class DrinkingGameListAPIView(ListAPIView):
    """Drinking Game List API View."""

    serializer_class = DrinkingGameSerializer
    queryset = DrinkingGame.objects.all()


class DrinkingGameRetrieveAPIView(RetrieveAPIView):
    """Drinking Game Retrieve API View."""

    serializer_class = DrinkingGameSerializer
    queryset = DrinkingGame.objects.all()
