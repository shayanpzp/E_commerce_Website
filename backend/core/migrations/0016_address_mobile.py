# Generated by Django 5.0.1 on 2024-02-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_cartorder_user_alter_productreview_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
