# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-02 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180702_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='maincontent',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcontent_a',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcontent_b',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcontent_c',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcontent_d',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcontent_e',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subimage_a',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subimage_b',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subimage_c',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subimage_d',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subimage_e',
        ),
    ]