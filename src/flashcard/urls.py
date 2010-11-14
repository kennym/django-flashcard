# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
    url(r'^$',
        views.list_flashcards,
        name = 'list_flashcards'),
    # FIXME: Make passing a string optional
    url(r'^practice/$',
        views.practice_flashcards,
        name = 'practice_flashcards'),
    url(r'^practice/(?P<mode>\w+)/$',
        views.practice_flashcards,
        name = 'practice_flashcards'),
    url(r'^rating/$',
        views.process_rating,
        name = 'process_rating'),
    url(r'^create/$',
        views.create_flashcard,
        name = 'create_flashcard'),
    url(r'^(\d+)/$',
        views.show_details_about,
        name = 'show_details'),
    url(r'^(\d+)/edit/$',
        views.edit_flashcard,
        name = 'edit_flashcard'),
    url(r'^(\d+)/delete/$',
        views.delete_flashcard,
        name = 'delete_flashcard'),
)
