# Generated by Django 5.0.6 on 2024-12-26 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_delete_orderplaced'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
