# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epi2', '0004_auto_20150924_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='trend_test',
            field=models.CharField(help_text='Enter result, if available (ex: p=0.015, p\u22640.05, n.s., etc.)', max_length=128, blank=True),
        ),
    ]