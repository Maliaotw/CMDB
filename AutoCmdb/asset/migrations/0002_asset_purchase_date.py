# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='購買日期'),
        ),
    ]
