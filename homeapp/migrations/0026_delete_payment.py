# Generated by Django 5.0.6 on 2025-01-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0025_rename_name_payment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='payment',
        ),
    ]
