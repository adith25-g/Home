# Generated by Django 5.0.6 on 2024-12-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0013_payment_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
