# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20151027_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='stage',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
