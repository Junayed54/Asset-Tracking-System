# Generated by Django 5.0.3 on 2024-04-02 16:04

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('serial_number', models.CharField(max_length=200)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('condition', models.CharField(default='Good', max_length=220)),
                ('checkout', models.BooleanField(default=False)),
                ('asset_issued', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='asset.company')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['serial_number'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('assets', models.ManyToManyField(to='asset.asset')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='asset.company')),
            ],
        ),
        migrations.CreateModel(
            name='AssetAssignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('assigned_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('return_notes', models.TextField()),
                ('asset_issued', models.BooleanField(default=False)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='asset.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='asset.employee')),
            ],
            options={
                'verbose_name': 'DeviceAssignment',
                'ordering': ('-updated_at',),
            },
        ),
    ]
