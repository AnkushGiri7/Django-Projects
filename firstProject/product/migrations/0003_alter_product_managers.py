# Generated by Django 5.0.1 on 2024-02-19 07:31

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_brand_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('pm', django.db.models.manager.Manager()),
            ],
        ),
    ]