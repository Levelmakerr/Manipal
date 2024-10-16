from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
   
class Location(models.Model):
    locationname = models.CharField(max_length=355, unique=True)
    
    def __str__(self):
        return self.locationname