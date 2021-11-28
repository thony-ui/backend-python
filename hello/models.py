from django.db import models

# Create your models here. Create a database here
class Feature(models.Model):
    name = models.CharField(max_length=150, default = 'some string')
    details = models.CharField(max_length=550, default = 'some string')