# Generated by Django 5.0.1 on 2024-02-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('current_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('facebook_link', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(max_length=255)),
                ('linkedin_link', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=255)),
                ('account_for', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
