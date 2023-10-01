# Generated by Django 4.2.5 on 2023-09-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageExtract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('regex', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('var_url_paginate', models.CharField(blank=True, max_length=250)),
                ('path_paginate', models.CharField(blank=True, max_length=250)),
                ('url_base', models.CharField(max_length=250)),
            ],
        ),
    ]