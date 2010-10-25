from django.db import models

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
