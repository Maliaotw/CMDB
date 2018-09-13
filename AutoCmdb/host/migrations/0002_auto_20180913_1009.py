# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='name',
        ),
        migrations.AddField(
            model_name='host',
            name='number',
            field=models.IntegerField(default=999, verbose_name='編號'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='host',
            name='ops_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.UserProfile', verbose_name='運維負責人'),
        ),
        migrations.AlterField(
            model_name='host',
            name='sn',
            field=models.CharField(db_index=True, max_length=64, verbose_name='SN序號'),
        ),
    ]
