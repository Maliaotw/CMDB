# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180913_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='部門名稱'),
        ),
    ]
