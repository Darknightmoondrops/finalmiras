# Generated by Django 4.0.4 on 2022-05-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Derakhti', '0013_mainuser_r_or_l'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='Payment Status'),
        ),
    ]
