# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-24 16:48


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("epi", "0008_exposure_numerical_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupresult",
            name="lower_range",
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name=b"Lower range",
                help_text="Numerical value for lower range",
            ),
        ),
        migrations.AddField(
            model_name="groupresult",
            name="upper_range",
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name=b"Upper range",
                help_text="Numerical value for upper range",
            ),
        ),
    ]