# -*- mode: python; coding: utf-8; -*-

from dj.dvoc.models import FlashCard
from django.contrib import admin

class FlashCardAdmin(admin.ModelAdmin):
    fields = ['front', 'back', 'easy_factor']
    list_display = ('front', 'back', 'easy_factor')

admin.site.register(FlashCard, FlashCardAdmin)
