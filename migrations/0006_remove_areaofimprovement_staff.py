# Generated by Django 3.1.1 on 2023-09-28 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20230928_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaofimprovement',
            name='staff',
        ),
    ]
