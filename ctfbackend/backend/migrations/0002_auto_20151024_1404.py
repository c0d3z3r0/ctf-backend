# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='short_name',
            field=models.CharField(default='', unique=True, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
