# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150930_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=255)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('count', models.CharField(max_length=255, null=True, blank=True)),
                ('state_abbrev', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.ForeignKey(blank=True, to='main.State', null=True)),
            ],
        ),
    ]
