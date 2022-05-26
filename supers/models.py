from django.db import models
from .models import Super
# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchpharse = models.CharField(max_length=255)
    super_type = models.ForeignKey(super, on_delete=models.CASCADE)