# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyHint',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name_plural': 'Bought Hints',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('difficulty', models.SmallIntegerField(default=1, choices=[(1, 'easy'), (2, 'medium'), (3, 'hard'), (4, 'very hard')])),
                ('active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='backend.Category')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('short_name', models.CharField(unique=True, max_length=15)),
                ('long_name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('flag', models.CharField(unique=True, max_length=100)),
                ('credits', models.PositiveIntegerField()),
                ('stage', models.PositiveIntegerField()),
                ('stage_description', models.TextField()),
                ('stage_link', models.URLField(blank=True)),
                ('challenge', models.ForeignKey(to='backend.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('flag', models.ForeignKey(to='backend.Flag')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='backend.BuyHint')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('semester', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(to='backend.Course')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('solution', models.TextField()),
                ('flag', models.ForeignKey(to='backend.Flag')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.AddField(
            model_name='flag',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='backend.Solve'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(to='backend.Faculty'),
        ),
        migrations.AddField(
            model_name='buyhint',
            name='hint',
            field=models.ForeignKey(to='backend.Hint'),
        ),
        migrations.AddField(
            model_name='buyhint',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='hint',
            unique_together=set([('order', 'flag')]),
        ),
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([('stage', 'challenge')]),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('short_name', 'long_name', 'faculty')]),
        ),
        migrations.AlterUniqueTogether(
            name='buyhint',
            unique_together=set([('hint', 'user')]),
        ),
    ]
