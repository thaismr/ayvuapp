from django.contrib import admin
from .models import (
    Vocabulary,
    PartOfSpeech,
    VocabularyDefinition,
    VocabularyExample
)


class VocabularyDefinitionInline(admin.StackedInline):
    model = VocabularyDefinition
    show_change_link = True
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'part_of_speech__language',
            'vocabulary',
        )


class VocabularyExampleInline(admin.StackedInline):
    model = VocabularyExample
    show_change_link = True
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'definition__part_of_speech__language',
            'definition__vocabulary'
        )


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    search_fields = ['word', ]
    autocomplete_fields = ('synonyms', 'publisher')
    list_display = ('word', 'public', 'language', 'level', 'publisher')
    list_select_related = ('language', 'publisher')

    inlines = [VocabularyDefinitionInline]


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

    inlines = [VocabularyExampleInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'part_of_speech__language', 'vocabulary'
        )


@admin.register(VocabularyExample)
class VocabularyExampleAdmin(admin.ModelAdmin):
    search_fields = ['example', 'definition__definition', 'definition__vocabulary__word']
    autocomplete_fields = ('definition',)
    list_select_related = (
        'definition__part_of_speech__language',
        'definition__vocabulary__language'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'definition__part_of_speech__language',
            'definition__vocabulary__language'
        )

