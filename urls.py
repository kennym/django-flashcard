# -*- mode: python; coding: utf-8; -*-

"""
A brief module description.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django.conf.urls.defaults import *

from dj.dvoc import views


urlpatterns = patterns('',
    url(r'^$',
        views.list_flashcards,
        name = 'list_flashcards'),
    url(r'^flashcards/(\d+)/$',
        views.show_details_about,
        name = 'show_details'),
    url(r'^create/$',
        views.create_flashcard,
        name = 'create_flashcard'),
)
