# Generated by Django 5.0.1 on 2024-01-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product_life_product_mfd_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='chat_resp_time',
            field=models.CharField(default='88', max_length=100),
        ),
    ]