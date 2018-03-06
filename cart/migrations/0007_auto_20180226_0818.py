# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_sub_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='sub_total',
            new_name='subtotal',
        ),
    ]
