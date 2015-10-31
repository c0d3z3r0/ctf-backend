# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_flag_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='stage_title',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
