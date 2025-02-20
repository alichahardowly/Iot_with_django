from django.db import models

class SmartDevice(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False) 
    topic = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return self.name
