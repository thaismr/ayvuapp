from django.contrib import admin
from .models import (
    Vocabulary,
    PartOfSpeech,
    VocabularyDefinition,
    VocabularyExample
)


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    search_fields = ['word', ]
    autocomplete_fields = ('synonyms',)


@admin.register(PartOfSpeech)
class PartOfSpeechAdmin(admin.ModelAdmin):
    search_fields = ['part_of_speech', ]


@admin.register(VocabularyDefinition)
class VocabularyDefinitionAdmin(admin.ModelAdmin):
    search_fields = ['definition', 'usage']


@admin.register(VocabularyExample)
class VocabularyExampleAdmin(admin.ModelAdmin):
    search_fields = ['example', ]

