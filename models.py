from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.forms import ModelForm, Textarea

class Practice(models.Model):
    """
    The Practice model.

    Its purpose is to track how much a user practiced an object, and how easy
    it is to him.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User)
    next_practice = models.DateField(auto_now_add=True)
    times_practiced = models.PositiveIntegerField(default=1)
    easy_factor = models.FloatField(default=2.5)

    def __unicode__(self):
        return "Flashcard (%s)" % self.item.front
    class Meta:
        ordering = ['next_practice']


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
    practice = generic.GenericForeignKey(Practice)

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
