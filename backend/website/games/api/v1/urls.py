from django.urls import path

from games.api.v1.views import DrinkingGameListAPIView, DrinkingGameRetrieveAPIView

urlpatterns = [
    path("", DrinkingGameListAPIView.as_view(), name="drinkinggame_list"),
    path("<int:pk>", DrinkingGameRetrieveAPIView.as_view(), name="drinkinggame_retrieve"),
]
