# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-09 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20180709_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postpictures',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='postpictures',
            name='width_field',
        ),
        migrations.AddField(
            model_name='postpictures',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AddField(
            model_name='postpictures',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AddField(
            model_name='postpictures',
            name='image_7',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AddField(
            model_name='postpictures',
            name='post_title',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='postpictures',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AlterField(
            model_name='postpictures',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AlterField(
            model_name='postpictures',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
        migrations.AlterField(
            model_name='postpictures',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location_pic),
        ),
    ]
