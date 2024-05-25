from django.db import models

# Create your models here.

class VisitCount(models.Model):
    ip_address=models.CharField(max_length=255)
    happen_time = models.DateTimeField(auto_now_add=True)

