# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_flag_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='file',
            field=models.FileField(upload_to='', blank=True),
        ),
    ]
