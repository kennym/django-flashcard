# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django.conf.urls.defaults import *

from dj.dvoc import views


urlpatterns = patterns('',
    url(r'^$',
        views.list_flashcards,
        name = 'list_flashcards'),
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
    url(r'^(\d+)/practice/$',
        views.practice_flashcard,
        name = 'practice_flashcard'),
)
