# Generated by Django 4.1.5 on 2023-03-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_alter_order_order_code_cartdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]