# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-04 13:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20180704_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertext',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 4, 13, 5, 36, 26953, tzinfo=utc)),
            preserve_default=False,
        ),
    ]