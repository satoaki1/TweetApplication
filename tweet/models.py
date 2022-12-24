from django.db import models
from django.utils import timezone
import uuid

app_name = 'tweet'


class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    tweet = models.TextField(verbose_name='tweet', max_length=140)
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now)
