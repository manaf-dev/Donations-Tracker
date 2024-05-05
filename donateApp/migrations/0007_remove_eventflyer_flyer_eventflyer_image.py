# Generated by Django 5.0.4 on 2024-05-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateApp', '0006_eventflyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventflyer',
            name='flyer',
        ),
        migrations.AddField(
            model_name='eventflyer',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='events_flyers'),
        ),
    ]
