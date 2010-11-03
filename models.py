from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea


class FlashCard(models.Model):
    """
    A basic Flashcard.

    Has a front and a back view.
    """
    front = models.TextField(
                    max_length = 255,
                    verbose_name = "Front")
    back = models.TextField(
                    max_length = 255,
                    verbose_name = "Back")
    user = models.ForeignKey(User)

    @models.permalink
    def get_absolute_url(self):
        return ('show_details', [str(self.id)])

    @models.permalink
    def edit(self):
        return ('edit_flashcard', [str(self.id)])

    @models.permalink
    def delete(self):
        return ('delete_flashcard', [str(self.id)])

    def __unicode__(self):
        return u"%s - %s" % (self.front, self.back)

    class Meta:
        verbose_name = "Flashcard"
        verbose_name_plural = "Flashcards"


class FlashCardForm(ModelForm):
    class Meta():
        model = FlashCard
        fields = ['front', 'back']
        exclude = ('user')
        widgets = {
            'front': Textarea(attrs={'cols': 70, 'rows': 10}),
            'back': Textarea(attrs={'cols': 70, 'rows': 10}),
        }
