from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ('vocabulary',)
