# Generated by Django 4.1 on 2023-10-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(verbose_name=False),
        ),
    ]