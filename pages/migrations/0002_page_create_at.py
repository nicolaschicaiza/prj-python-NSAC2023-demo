# Generated by Django 4.1 on 2023-10-02 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='create_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
