from django.db import models
from django.conf import settings
from jdatetime import datetime as dt
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=dt.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
            self.published_date = dt.now()
            self.save()

    def __str__(self):
            return self.title +str(self.created_date)