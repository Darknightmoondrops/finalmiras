# Generated by Django 4.0.4 on 2022-05-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taksathi', '0010_alter_productsorders_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='Products', verbose_name='Image1'),
        ),
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='Products', verbose_name='Image2'),
        ),
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='Products', verbose_name='Image3'),
        ),
    ]
