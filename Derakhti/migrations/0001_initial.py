# Generated by Django 4.0.4 on 2022-05-07 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifierـcode', models.CharField(max_length=30, unique=True, verbose_name='Identifier code')),
                ('places', models.IntegerField(default=1, verbose_name='Places')),
                ('Owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
    ]
