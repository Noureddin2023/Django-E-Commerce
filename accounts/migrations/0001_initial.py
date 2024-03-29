# Generated by Django 4.1.5 on 2023-04-13 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile/')),
                ('code', models.CharField(default=utils.generate_code.generate_code, max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Primary', 'Primary'), ('Secondery', 'Secondery')], max_length=10)),
                ('number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='user_contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Bussiness', 'Bussiness'), ('Academy', 'Academy'), ('Others', 'Othres')], max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('house', models.CharField(max_length=20)),
                ('notes', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='user_contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
