# Generated by Django 5.0.4 on 2024-05-31 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateApp', '0002_event_flyer_alter_donation_event_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['is_completed', '-date_created'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='event',
            name='thank_you_msg',
            field=models.TextField(blank=True, default='We appreciate your kindness.'),
        ),
    ]
