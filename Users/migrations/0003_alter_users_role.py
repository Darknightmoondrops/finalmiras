# Generated by Django 4.0.4 on 2022-05-05 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_users_dateـofـbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('derakhti', 'derakhti'), ('mlm', 'mlm'), ('taksathi', 'taksathi'), ('taksathiAdmin', 'taksathiAdmin')], max_length=50, verbose_name='Rols'),
        ),
    ]
