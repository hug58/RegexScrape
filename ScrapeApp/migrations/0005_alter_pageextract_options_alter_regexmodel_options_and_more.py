# Generated by Django 4.2.5 on 2023-10-01 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapeApp', '0004_alter_pageextract_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageextract',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='regexmodel',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='pageextract',
            name='is_paginational',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regexmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regexmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]