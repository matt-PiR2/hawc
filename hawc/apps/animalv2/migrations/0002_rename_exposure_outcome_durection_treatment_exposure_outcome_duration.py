# Generated by Django 5.0 on 2024-01-22 17:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("animalv2", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="treatment",
            old_name="exposure_outcome_durection",
            new_name="exposure_outcome_duration",
        ),
    ]
