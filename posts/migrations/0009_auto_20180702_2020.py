# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-02 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_maincontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='content123',
        ),
    ]
