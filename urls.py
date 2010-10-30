# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django.conf.urls.defaults import *

from dj.dvoc import views

from memorize.views import next_practice_item


urlpatterns = patterns('',
    url(r'^$',
        views.list_flashcards,
        name = 'list_flashcards'),
    url(r'^flashcard/(\d+)/$',
        views.show_details_about,
        name = 'show_details'),
    url(r'^flashcard/(\d+)/edit/$',
        views.edit_flashcard,
        name = 'edit_flashcard'),
    url(r'^flashcard/(\d+)/delete/$',
        views.delete_flashcard,
        name = 'delete_flashcard'),
    url(r'^flashcard/create/$',
        views.create_flashcard,
        name = 'create_flashcard'),
    url(r'^flashcard/next/$',
        next_practice_item,
        {'template': 'memorize/next.html'},
        name='next-flashcard')
)
