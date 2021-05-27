from django.db import models
from tinymce.models import HTMLField


class Item(models.Model):
    """Necessity model."""

    name = models.CharField(max_length=1024, help_text="The name of the item")

    def __str__(self):
        """Convert this object to string."""
        return self.name


class DrinkingGame(models.Model):
    """Drinking Game model."""

    name = models.CharField(max_length=1024, help_text="The name of the drinking game.")
    description = HTMLField(help_text="The description of how to play the drinking game.")
    items = models.ManyToManyField(Item, help_text="The items needed to play this drinking game.", blank=True)

    def __str__(self):
        """Convert this object to string."""
        return self.name
