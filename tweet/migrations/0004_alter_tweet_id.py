# Generated by Django 4.1.4 on 2022-12-24 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_alter_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cd9dfeb9-4184-416f-ae64-edd2f1efb01b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
