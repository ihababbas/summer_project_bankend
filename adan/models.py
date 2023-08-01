from django.db import models

# Create your models here.
class adan(models.Model):
    pray = models.CharField(max_length=255)
    time = models.DecimalField(max_digits=10, decimal_places=2)