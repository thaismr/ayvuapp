# Generated by Django 4.0.4 on 2022-04-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmaterial',
            name='url',
            field=models.URLField(blank=True,
                                  default=None,
                                  null=True,
                                  verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='material',
            name='url',
            field=models.URLField(blank=True,
                                  default=None,
                                  null=True,
                                  verbose_name='URL'),
        ),
    ]
