from django.contrib import admin
from django.contrib.admin import ModelAdmin

from games import models


@admin.register(models.DrinkingGame)
class DrinkingGameAdmin(ModelAdmin):
    """Drinking Game Admin."""

    pass


@admin.register(models.Item)
class ItemAdmin(ModelAdmin):
    """Item Admin."""

    pass
