# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def clear_empty_descriptions(apps, schema_editor):
    Challenge = apps.get_model("backend", "Challenge")
    db_alias = schema_editor.connection.alias
    challenges = Challenge.objects.using(db_alias).filter(description=' ')
    for challenge in challenges:
        challenge.description = ''
        challenge.save()


def undo(*args, **kwargs):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20151031_2259'),
    ]

    operations = [
        migrations.RunPython(clear_empty_descriptions, undo),
    ]