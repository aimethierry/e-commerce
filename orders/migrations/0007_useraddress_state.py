# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180309_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='state',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
