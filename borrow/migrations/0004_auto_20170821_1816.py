# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 12:46
from __future__ import unicode_literals

import borrow.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0003_auto_20170821_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='approved',
            field=models.NullBooleanField(default=borrow.models.approved_default),
        ),
    ]
