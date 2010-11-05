# -*- mode: python; coding: utf-8; -*-

from models import FlashCard, Practice
from django.contrib import admin

class FlashCardAdmin(admin.ModelAdmin):
    fields = ['front', 'back', 'user']
    list_display = ('front', 'back', 'user')

class PracticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(FlashCard, FlashCardAdmin)
admin.site.register(Practice, PracticeAdmin)
