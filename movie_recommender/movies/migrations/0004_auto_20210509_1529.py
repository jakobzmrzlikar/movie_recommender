# Generated by Django 3.0.3 on 2021-05-09 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210509_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='view',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]