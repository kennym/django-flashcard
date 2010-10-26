from django.db import models
from django.forms import ModelForm

class FlashCard(models.Model):
    """
    A basic Flashcard

    Has a front and a back view.
    """
    front_view = models.CharField(
                    max_length = 200,
                    verbose_name = "Front")
    back_view = models.CharField(
                    max_length = 200,
                    verbose_name = "Back")

class FlashCardForm(ModelForm):
    class Meta:
        model = FlashCard
