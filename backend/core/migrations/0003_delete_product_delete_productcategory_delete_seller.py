# Generated by Django 5.0.1 on 2024-01-15 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_productcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
