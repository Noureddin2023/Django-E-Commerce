# Generated by Django 4.1.5 on 2023-01-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]