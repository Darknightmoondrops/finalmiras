# Generated by Django 4.0.4 on 2022-05-07 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Derakhti', '0002_rusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='Owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mainUser_owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
