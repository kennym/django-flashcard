# -*- mode: python; coding: utf-8; -*-

from dj.dvoc.models import FlashCard
from django.contrib import admin

class FlashCardAdmin(admin.ModelAdmin):
    fields = ['front', 'back', 'user']
    list_display = ('front', 'back', 'user')

admin.site.register(FlashCard, FlashCardAdmin)
