# Generated by Django 5.2.1 on 2025-05-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0016_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
