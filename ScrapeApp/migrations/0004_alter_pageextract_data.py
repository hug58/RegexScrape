# Generated by Django 4.2.5 on 2023-09-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapeApp', '0003_rename_regex_regexmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageextract',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
