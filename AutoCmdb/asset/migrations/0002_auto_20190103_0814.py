# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-03 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetrepairdetail',
            options={'verbose_name_plural': '資產維修詳細紀錄表'},
        ),
        migrations.RemoveField(
            model_name='assetrepairdetail',
            name='record',
        ),
        migrations.AddField(
            model_name='assetrepairdetail',
            name='repair',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asset.AssetRepair'),
            preserve_default=False,
        ),
    ]
