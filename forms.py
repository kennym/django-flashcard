# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django import forms
from django.core.exceptions import ValidationError

RATINGS = ((0, 'Blackout'), (1, 'Barely Know it'), (2, 'Needs Work'),
           (3, 'Remembered'), (4, 'Solid'))


class RatingForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    rating = forms.ChoiceField(choices=RATINGS)

# vim: ai ts=4 sts=4 et sw=4
