# Generated by Django 5.2.1 on 2025-05-31 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_is_futured'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='service',
        ),
    ]
