from django.contrib import admin
from .models import Vocabulary


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    search_fields = ['word', 'definition']
    autocomplete_fields = ('synonyms',)
