# Generated by Django 5.0.4 on 2024-05-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.IntegerField(),
        ),
    ]