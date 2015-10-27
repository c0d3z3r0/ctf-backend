# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20151024_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
