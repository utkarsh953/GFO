# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-09 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_postpictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpictures',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postpictures',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
