# Generated by Django 2.2.15 on 2020-08-27 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vocab", "0001_initial"),
        ("animal", "0027_endpoint_ordering"),
    ]

    operations = [
        migrations.AddField(
            model_name="endpoint",
            name="effect_subtype_term",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_effect_subtype_terms",
                to="vocab.Term",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="effect_term",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_effect_terms",
                to="vocab.Term",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="organ_term",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_organ_terms",
                to="vocab.Term",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="system_term",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_system_terms",
                to="vocab.Term",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="name_term",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_name_terms",
                to="vocab.Term",
            ),
        ),
    ]