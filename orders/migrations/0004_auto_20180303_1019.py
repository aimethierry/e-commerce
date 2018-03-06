# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_useradress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=150, choices=[(b'billing', b'billing'), (b'shipping', b'shipping')])),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
        migrations.RemoveField(
            model_name='useradress',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAdress',
        ),
    ]
