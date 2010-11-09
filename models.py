from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.forms import ModelForm, Textarea

from datetime import date, timedelta

from algorithm import interval


class FlashCardPracticeManager(models.Manager):
    def get_query_set(self):
        return FlashCard.objects.all().order_by('next_practice')


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

    next_practice = models.DateField(auto_now_add=True)
    times_practiced = models.PositiveIntegerField(default=1)
    easy_factor = models.FloatField(default=2.5)

    # Managers
    objects = models.Manager()
    by_practice = FlashCardPracticeManager()
    by_easy_factor = None # TODO
    by_times_practiced = None # TODO

    @models.permalink
    def get_absolute_url(self):
        return ('show_details', [str(self.id)])

    @models.permalink
    def edit(self):
        return ('edit_flashcard', [str(self.id)])

    @models.permalink
    def delete(self):
        return ('delete_flashcard', [str(self.id)])

    def set_next_practice(self, rating):
        days, ef = interval(self.times_practiced, rating,
                            self.easy_factor)
        self.next_practice = date.today() + timedelta(days=days)
        self.times_practiced += 1
        self.easy_factor = ef

    def delay(self):
        self.next_practice = date.today() + timedelta(days=1)

    def __unicode__(self):
        return u"%s - %s" % (self.front, self.back)

    def __str__(self):
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
