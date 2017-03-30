from django.db import models
from django.utils import timezone

# Create your models here.
class Flower(models.Model):
	flower_id = models.BigIntegerField()
	description = models.CharField(max_length=200)
	foto_linl = models.CharField(max_length=200)
