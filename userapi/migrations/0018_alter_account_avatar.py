# Generated by Django 5.2.1 on 2025-05-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0017_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6cO4QNRFwPkLwBjfA-X13VvKJC1hU22i9NajNmhExaCxU6dgGLTvfGawVXGOT8SpvZ3M&usqp=CAU', null=True, upload_to='avatars/'),
        ),
    ]
