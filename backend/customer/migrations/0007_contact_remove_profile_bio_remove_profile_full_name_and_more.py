# Generated by Django 5.0.3 on 2024-03-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('massage', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='verified',
        ),
    ]