# Generated by Django 5.2.1 on 2025-05-14 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_remove_account_created_account_binance_usd_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balance',
        ),
    ]
