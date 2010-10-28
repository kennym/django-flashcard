from django.db import models
from django.forms import ModelForm


class FlashCard(models.Model):
    """
    A basic Flashcard.

    Has a front and a back view.
    """
    front = models.CharField(
                    max_length = 200,
                    verbose_name = "Front")
    back = models.CharField(
                    max_length = 200,
                    verbose_name = "Back")

    @models.permalink
    def get_absolute_url(self):
        return ('show_details', [str(self.id)])
    
    def __unicode__(self):
        return u"%s - %s" % (self.front, self.back)

class FlashCardForm(ModelForm):
    class Meta:
        model = FlashCard
