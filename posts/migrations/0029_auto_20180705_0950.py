# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-05 09:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20180705_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggerprofile',
            name='image',
            field=models.CharField(blank=True, default=datetime.datetime(2018, 7, 5, 9, 50, 25, 22253, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
