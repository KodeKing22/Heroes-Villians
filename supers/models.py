from django.db import models
from super_types.models import SuperTypes

# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchpharse = models.CharField(max_length=255, blank=True, null=True)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.CASCADE, null=True)
