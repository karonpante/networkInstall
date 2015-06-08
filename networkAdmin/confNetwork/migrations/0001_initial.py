# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceContainsVlanGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device', models.ForeignKey(to='confNetwork.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceContainsVlans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device', models.ForeignKey(to='confNetwork.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VlanGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VlanGroupContainsVlans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vlan', models.ForeignKey(to='confNetwork.Vlan')),
                ('vlanGroup', models.ForeignKey(to='confNetwork.VlanGroup')),
            ],
        ),
        migrations.AddField(
            model_name='devicecontainsvlans',
            name='vlan',
            field=models.ForeignKey(to='confNetwork.Vlan'),
        ),
        migrations.AddField(
            model_name='devicecontainsvlangroups',
            name='vlanGroup',
            field=models.ForeignKey(to='confNetwork.VlanGroup'),
        ),
        migrations.AddField(
            model_name='device',
            name='environment',
            field=models.ForeignKey(to='confNetwork.Environment'),
        ),
    ]
