from django.db import models

# Create your models here.

class ShowCase(models.Model):
    url=models.CharField(max_length=255)
    likeCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
