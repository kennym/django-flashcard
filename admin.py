# -*- mode: python; coding: utf-8; -*-

from dj.dvoc.models import FlashCard
from django.contrib import admin

class FlashCardAdmin(admin.ModelAdmin):
    fields = ['front_view', 'back_view']
    list_display = ('front_view', 'back_view')

admin.site.register(FlashCard, FlashCardAdmin)
