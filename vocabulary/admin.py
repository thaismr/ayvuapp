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
    list_display = ('part_of_speech', 'language')
    list_filter = ('language__code',)
    search_fields = ['part_of_speech', ]


@admin.register(VocabularyDefinition)
class VocabularyDefinitionAdmin(admin.ModelAdmin):
    search_fields = ['vocabulary__word', 'part_of_speech__part_of_speech', 'definition', 'usage']
    autocomplete_fields = ('part_of_speech', 'vocabulary',)
    list_display = ('vocabulary', 'part_of_speech', 'definition', 'usage')
    list_filter = ('part_of_speech__part_of_speech', 'vocabulary__language__code',)


@admin.register(VocabularyExample)
class VocabularyExampleAdmin(admin.ModelAdmin):
    search_fields = ['example', ]

