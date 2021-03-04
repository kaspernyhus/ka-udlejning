# Generated by Django 3.1.7 on 2021-03-04 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betaling',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='tankning',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='ture',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='udgift',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='betaling',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tankning',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='ture',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='udgift',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]