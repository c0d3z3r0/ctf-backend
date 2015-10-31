# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_flag_stage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='file',
        ),
        migrations.RemoveField(
            model_name='flag',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='challenge',
            field=models.ForeignKey(to='backend.Challenge', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='stage',
            field=models.ForeignKey(to='backend.Flag', null=True, blank=True),
        ),
    ]
