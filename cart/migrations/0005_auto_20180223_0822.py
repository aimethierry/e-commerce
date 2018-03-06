# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem_line_item_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
        ),
    ]
