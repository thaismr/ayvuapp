from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ('vocabulary',)
