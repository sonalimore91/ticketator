# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 13:21
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170201_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
        migrations.RemoveField(
            model_name='logs',
            name='log_date',
        ),
        migrations.RemoveField(
            model_name='microtasks',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
        migrations.AddField(
            model_name='attachment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='inventorygroup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventorygroup',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='logs',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='microtasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='microtasks',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='priority',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priority',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='queue',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='queue',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='rights',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rights',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='state',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='usertype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]