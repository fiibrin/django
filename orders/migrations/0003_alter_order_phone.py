# Generated by Django 4.1.7 on 2023-05-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='+7', max_length=13),
        ),
    ]