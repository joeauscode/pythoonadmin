# Generated by Django 5.2.1 on 2025-05-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0007_rename_date_deposithistory_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
