# Generated by Django 5.0.1 on 2024-02-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]