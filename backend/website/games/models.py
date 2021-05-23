from django.db import models


class Item(models.Model):
    """Necessity model."""

    name = models.CharField(max_length=1024, help_text="The name of the item")


class DrinkingGame(models.Model):
    """Drinking Game model."""

    name = models.CharField(max_length=1024, help_text="The name of the drinking game.")
    description = models.TextField(help_text="The description of how to play the drinking game.")
    items = models.ManyToManyField(Item, help_text="The items needed to play this drinking game.")
