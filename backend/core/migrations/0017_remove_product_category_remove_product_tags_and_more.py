# Generated by Django 5.0.3 on 2024-03-15 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_address_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
    ]
