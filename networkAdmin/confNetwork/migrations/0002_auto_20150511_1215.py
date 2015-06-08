# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confNetwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='ip',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
