# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_challenge_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='link',
        ),
        migrations.RemoveField(
            model_name='flag',
            name='stage_link',
        ),
    ]
