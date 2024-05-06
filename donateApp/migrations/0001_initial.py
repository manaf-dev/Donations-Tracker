# Generated by Django 5.0.4 on 2024-05-03 10:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_num', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Donors',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.CharField(max_length=50, unique=True, null=False)),
                ('is_completed', models.BooleanField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donateApp.donor')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donateApp.event')),
            ],
            options={
                'verbose_name_plural': 'Donations',
            },
        ),
    ]
