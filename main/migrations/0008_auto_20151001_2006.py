# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='count',
            new_name='county',
        ),
    ]
