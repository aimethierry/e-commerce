# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180202_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='productFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=product.models.image_upload_to_featured)),
                ('title', models.CharField(max_length=140, null=True, blank=True)),
                ('text', models.CharField(max_length=240, null=True, blank=True)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-title']},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='product.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=product.models.image_upload_to),
        ),
        migrations.AddField(
            model_name='productfeatured',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]
