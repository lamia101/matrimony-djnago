# Generated by Django 5.0.1 on 2024-02-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('current_address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('facebook_link', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=255)),
                ('account_for', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
