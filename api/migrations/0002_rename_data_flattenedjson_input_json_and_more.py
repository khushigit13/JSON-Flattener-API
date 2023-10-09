# Generated by Django 4.2.6 on 2023-10-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flattenedjson',
            old_name='data',
            new_name='input_json',
        ),
        migrations.AddField(
            model_name='flattenedjson',
            name='flattened_json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
