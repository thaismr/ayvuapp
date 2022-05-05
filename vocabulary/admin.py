from django.contrib import admin
from .models import Vocabulary


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    search_fields = ['word', 'definition', 'language']
    autocomplete_fields = ['synonyms']
