# Generated by Django 4.1.2 on 2022-10-29 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_public_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.CharField(default='cold', max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='public_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 29, 0, 4, 5, 155609, tzinfo=datetime.timezone.utc)),
        ),
    ]