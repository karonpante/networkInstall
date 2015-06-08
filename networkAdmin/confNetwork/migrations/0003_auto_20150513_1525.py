# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confNetwork', '0002_auto_20150511_1215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Environment',
            new_name='Datacenter',
        ),
        migrations.RemoveField(
            model_name='device',
            name='environment',
        ),
        migrations.AddField(
            model_name='device',
            name='datacenter',
            field=models.ForeignKey(default=1, to='confNetwork.Datacenter'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='datacenter',
            field=models.ForeignKey(default=1, to='confNetwork.Datacenter'),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='datacenter',
            field=models.ForeignKey(default=1, to='confNetwork.Datacenter'),
        ),
    ]
