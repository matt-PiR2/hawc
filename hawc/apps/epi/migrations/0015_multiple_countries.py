# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-11-26 21:26
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_countries_m2m(apps, schema_editor):
    StudyPopulation = apps.get_model("epi", "StudyPopulation")
    for sp in StudyPopulation.objects.all():
        print(f"SP{sp.id} from {sp.country.id}.{sp.country.code}.{sp.country.name}")
        sp.countries.add(sp.country)
        sp.save()


class Migration(migrations.Migration):

    dependencies = [
        ("epi", "0014_delete_exposure_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="studypopulation",
            name="countries",
            field=models.ManyToManyField(blank=True, to="epi.Country"),
        ),
        migrations.RunPython(migrate_countries_m2m),
        migrations.RemoveField(model_name="studypopulation", name="country",),
    ]