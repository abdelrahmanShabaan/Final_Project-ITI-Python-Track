# Generated by Django 5.0.3 on 2024-03-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('seller', 'Seller'), ('customer', 'Customer')], max_length=15)),
                ('validation_states', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('code', models.CharField(default=0, max_length=6)),
                ('expireTime', models.DateTimeField()),
            ],
        ),
    ]
