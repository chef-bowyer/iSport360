# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetaTester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=2)),
                ('coach', models.BooleanField()),
                ('parent', models.BooleanField()),
                ('soccer', models.BooleanField()),
                ('baseball', models.BooleanField()),
                ('softball', models.BooleanField()),
                ('lacrosse', models.BooleanField()),
                ('basketball', models.BooleanField()),
                ('volleyball', models.BooleanField()),
                ('football', models.BooleanField()),
                ('golf', models.BooleanField()),
                ('tennis', models.BooleanField()),
                ('ice_skating', models.BooleanField()),
                ('swimming', models.BooleanField()),
                ('gymnastics', models.BooleanField()),
                ('other', models.CharField(max_length=32)),
            ],
        ),
    ]
