# Generated by Django 4.0.4 on 2022-05-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taksathi', '0002_alter_tiket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiket',
            name='status',
            field=models.BooleanField(blank=True, default=False, verbose_name='Status'),
        ),
    ]
