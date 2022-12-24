# Generated by Django 4.1.4 on 2022-12-24 01:54

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('39f88a70-2fd2-4977-89c4-c16ec78fe310'), editable=False, primary_key=True, serialize=False)),
                ('tweet', models.TextField(max_length=140, verbose_name='tweet')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 24, 1, 54, 52, 966206, tzinfo=datetime.timezone.utc), verbose_name='Created at')),
            ],
        ),
    ]
