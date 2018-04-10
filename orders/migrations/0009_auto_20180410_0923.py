# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercheckout',
            name='braintree_id',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')]),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(blank=True, to='orders.UserCheckout', null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='zipcode',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
