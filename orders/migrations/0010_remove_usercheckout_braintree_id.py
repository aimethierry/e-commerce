# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180410_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercheckout',
            name='braintree_id',
        ),
    ]
