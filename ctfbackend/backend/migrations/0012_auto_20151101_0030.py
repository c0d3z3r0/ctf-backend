# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_clear_empty_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flag',
            old_name='stage_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='flag',
            old_name='stage_title',
            new_name='title',
        ),
    ]
