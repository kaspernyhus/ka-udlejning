# Generated by Django 3.1.7 on 2021-03-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KmPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=2.0)),
            ],
            options={
                'verbose_name_plural': 'Km-Price',
            },
        ),
    ]
