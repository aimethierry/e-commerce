# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20180223_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sub_total',
            field=models.DecimalField(default=1, max_digits=50, decimal_places=2),
        ),
    ]
