# Generated by Django 4.1.5 on 2023-02-08 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='addresse',
            new_name='address',
        ),
    ]
