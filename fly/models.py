from django.db import models

# Create your models here.

class dbfly(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    check = models.CharField(max_length=50, null=False) 
    memo = models.CharField(max_length=100, null=False)
    phase = models.CharField(max_length=50, null=False)
    lesson = models.CharField(max_length=100, null=False)
    

    def __str__(self):
	    return self.name