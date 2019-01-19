# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-19 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='設備名稱')),
                ('cctv_type', models.CharField(choices=[('NVR', 'NVR'), ('DVR', 'DVR'), ('IPCAM', 'IPCAM')], default=2, max_length=64, verbose_name='設備類型')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='內網IP')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='SN號')),
                ('manufactory', models.CharField(blank=True, max_length=128, null=True, verbose_name='製造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型號')),
                ('latest_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='創建日期')),
                ('warranty_date', models.DateField(blank=True, null=True, verbose_name='保固日期')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': 'CCTV',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=8, verbose_name='插槽位置')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='硬盤型號')),
                ('capacity', models.FloatField(verbose_name='硬盤容量')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='硬碟序號')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='製造商')),
                ('iface_type', models.CharField(max_length=64, verbose_name='接口類型')),
            ],
            options={
                'verbose_name_plural': '硬盤表',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('工作站', '工作站'), ('值班電腦', '值班電腦'), ('培訓電腦', '培訓電腦'), ('備用電腦', '備用電腦'), ('汰換機', '汰換機'), ('測試機', '測試機')], default='值班電腦', max_length=64)),
                ('name', models.CharField(max_length=64, verbose_name='主機名稱')),
                ('number', models.IntegerField(verbose_name='主機號碼')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='SN序號')),
                ('pn', models.CharField(blank=True, max_length=64, null=True, verbose_name='產品序號')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='製造商')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='型號')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='發行版本')),
                ('os_platform', models.CharField(blank=True, max_length=16, null=True, verbose_name='系統')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='系統版本')),
                ('cpu_count', models.IntegerField(blank=True, null=True, verbose_name='邏輯處理器')),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True, verbose_name='處理器內核')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='處理器型號')),
                ('asset', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Host', to='asset.Asset', verbose_name='資產編號')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Location', verbose_name='位置')),
                ('ops_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.UserProfile', verbose_name='運維負責人')),
            ],
            options={
                'verbose_name_plural': '主機資產表',
            },
        ),
        migrations.CreateModel(
            name='HostRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, '自動上傳'), (2, 'IT維護')], default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='創建日期')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='asset.UserProfile', verbose_name='創建者')),
                ('host_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.Host')),
            ],
            options={
                'verbose_name_plural': '主機紀錄表',
            },
        ),
        migrations.CreateModel(
            name='IPPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='設備名稱')),
                ('cctv_type', models.CharField(choices=[('NVR', 'NVR'), ('DVR', 'DVR'), ('IPCAM', 'IPCAM')], default=2, max_length=64, verbose_name='設備類型')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='內網IP')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='SN號')),
                ('manufactory', models.CharField(blank=True, max_length=128, null=True, verbose_name='製造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型號')),
                ('latest_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='創建日期')),
                ('warranty_date', models.DateField(blank=True, null=True, verbose_name='保固日期')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': 'IP電話',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位置')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='製造商')),
                ('model', models.CharField(max_length=64, verbose_name='型號')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='內存容量')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='內存SN號')),
                ('host_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='host.Host')),
            ],
            options={
                'verbose_name_plural': '内存表',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_asset_type', models.SmallIntegerField(choices=[('路由器', '路由器'), ('交換器', '交換器'), ('AP', 'AP'), ('防火牆', '防火牆')], default=0, verbose_name='設備類型')),
                ('name', models.CharField(max_length=64, verbose_name='設備名稱')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='內網IP')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='SN號')),
                ('manufactory', models.CharField(blank=True, max_length=128, null=True, verbose_name='製造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型號')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口個數')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('latest_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='創建日期')),
                ('warranty_date', models.DateField(blank=True, null=True, verbose_name='保固日期')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '網絡設備',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='網卡名稱')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='型號')),
                ('macaddress', models.CharField(blank=True, max_length=255, null=True, verbose_name='MAC')),
                ('netmask', models.CharField(blank=True, max_length=255, null=True, verbose_name='Netmask')),
                ('host_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='host.Host')),
            ],
            options={
                'verbose_name_plural': '網卡表',
            },
        ),
        migrations.AddField(
            model_name='disk',
            name='host_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='host.Host'),
        ),
    ]
