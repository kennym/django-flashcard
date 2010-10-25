# -*- mode: python; coding: utf-8; -*-

"""
A brief module description.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

#######################################################################
# IMPORTS                                                             #
#######################################################################

from django.conf.urls.defaults import *
from dj.dvoc import views

urlpatterns = patterns('',
    url(r'^$',
        views.flashcard_list,
        name = 'flascard_list'),
    url(r'^create/$',
        views.create_flashcard,
        name = 'create_flashcard'))
