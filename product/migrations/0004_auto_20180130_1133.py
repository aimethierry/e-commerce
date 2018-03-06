# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='Product',
            new_name='product',
        ),
    ]
