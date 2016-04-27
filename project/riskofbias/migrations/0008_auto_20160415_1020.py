# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riskofbias', '0007_split_rob_robscore_20160414_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskofbias',
            name='metric',
        ),
        migrations.RemoveField(
            model_name='riskofbias',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='riskofbias',
            name='score',
        ),
        migrations.AlterField(
            model_name='riskofbiasscore',
            name='riskofbias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='riskofbias.RiskOfBias'),
        ),
        migrations.AlterField(
            model_name='riskofbias',
            name='study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riskofbiases', to='study.Study'),
        ),
        migrations.AlterField(
            model_name='riskofbiasdomain',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rob_domains', to='assessment.Assessment'),
        ),
        migrations.AlterModelOptions(
            name='riskofbias',
            options={'ordering': ('conflict_resolution',), 'verbose_name_plural': 'Risk of Biases'},
        ),
    ]
