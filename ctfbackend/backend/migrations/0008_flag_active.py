# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20151028_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
