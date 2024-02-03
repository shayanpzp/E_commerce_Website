# Generated by Django 5.0.1 on 2024-02-03 03:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product.', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am a amazing vendor.', null=True),
        ),
    ]
