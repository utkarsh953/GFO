# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-03 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20180703_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloggerprofile',
            options={'verbose_name_plural': 'Bloggers'},
        ),
        migrations.AlterField(
            model_name='bloggerprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='BloggerProfile/'),
        ),
    ]
