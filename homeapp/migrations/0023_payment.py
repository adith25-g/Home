# Generated by Django 5.0.6 on 2025-01-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0022_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
