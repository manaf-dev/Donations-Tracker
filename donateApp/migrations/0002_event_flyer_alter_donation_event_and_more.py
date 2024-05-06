# Generated by Django 5.0.4 on 2024-05-06 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='flyer',
            field=models.ImageField(default='default.png', upload_to='events_flyers'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='donateApp.event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
