# Generated by Django 4.0.4 on 2022-04-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_historicaluserprofile_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='gender',
            field=models.CharField(blank=True,
                                   choices=[('F', 'Female'), ('M', 'Male'),
                                            ('O', 'Other')],
                                   default=None,
                                   max_length=1,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True,
                                   choices=[('F', 'Female'), ('M', 'Male'),
                                            ('O', 'Other')],
                                   default=None,
                                   max_length=1,
                                   null=True),
        ),
    ]
