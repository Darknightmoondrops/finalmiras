# Generated by Django 4.0.4 on 2022-05-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_users_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Book_or_buy_goods',
            field=models.BooleanField(default=False, verbose_name='Book or buy goods'),
        ),
    ]
