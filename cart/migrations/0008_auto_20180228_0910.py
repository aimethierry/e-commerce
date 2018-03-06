# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20180226_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=0.085, max_digits=10, decimal_places=5),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=25.0, max_digits=50, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=25.0, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=25.0, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
