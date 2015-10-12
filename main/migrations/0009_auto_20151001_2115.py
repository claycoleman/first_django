# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151001_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='zip_code',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
