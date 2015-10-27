# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20151027_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='stage_description',
            field=models.TextField(blank=True),
        ),
    ]
