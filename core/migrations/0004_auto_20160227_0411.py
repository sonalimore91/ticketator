# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(upload_to='./avatar/'),
        ),
    ]
