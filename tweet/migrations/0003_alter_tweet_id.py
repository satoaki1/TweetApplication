# Generated by Django 4.1.4 on 2022-12-24 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_alter_tweet_created_at_alter_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e8e7bb3-92e9-4d64-9c3f-4f8a0ce91cfd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
