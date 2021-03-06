# Generated by Django 4.0.4 on 2022-04-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name', models.CharField(max_length=50,
                                          verbose_name='Language')),
                ('slug', models.SlugField(unique=True)),
                ('flag',
                 models.ImageField(blank=True,
                                   null=True,
                                   upload_to='images/flags')),
                ('summary', models.CharField(blank=True, max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
