# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20180219_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
