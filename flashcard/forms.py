# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django.forms import ModelForm, Textarea
from django import forms
from django.core.exceptions import ValidationError

from models import FlashCard


RATINGS = ((0, 'Blackout'), 
           (1, 'Barely Know it'), 
           (2, 'Needs Work'),
           (3, 'Remembered'), 
           (4, 'Solid'))


class RatingForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    rating = forms.ChoiceField(choices=RATINGS)

SORTING = ((0, 'By alphabet'),
           (1, 'By next practice'))

class SortFlashcardsForm(forms.Form):
    sort_by = forms.ChoiceField(choices=SORTING)


class FlashCardForm(ModelForm):
    class Meta():
        model = FlashCard
        fields = ['front', 'back']
        exclude = ('user')
        widgets = {
            'front': Textarea(attrs={'cols': 70, 'rows': 10}),
            'back': Textarea(attrs={'cols': 70, 'rows': 10}),
        }


# vim: ai ts=4 sts=4 et sw=4
