# Generated by Django 4.0.4 on 2022-04-22 00:55
from django.db import migrations


def add_default(apps, schema_editor):
    """Set default language available"""
    Language = apps.get_model('languages', 'Language')
    default_language = Language(name='English', slug='en')
    default_language.save()


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default),
    ]
