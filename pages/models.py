from django.db import models
from rest_framework import serializers

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100,)
    MU = models.DecimalField(max_digits=8,decimal_places=3)
    U_ID = models.CharField(max_length=100,default='---')
    csv = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Data'

