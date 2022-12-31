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


class dblucy(models.Model):
    name = models.CharField(max_length=50,null=False)
    image = models.CharField(max_length=50, blank=True , default=' ')
    sound = models.CharField(max_length=100, blank=True , default=' ')
    bgcolor = models.CharField(max_length=50, blank=True , default=' ')
    textsize = models.CharField(max_length=50, blank=True , default=' ')
    type = models.CharField(max_length=50, blank=True , default=' ')
    status = models.CharField(max_length=50, blank=True , default=' ')
    data = models.CharField(max_length=200, blank=True , default=' ')
    

    def __str__(self):
	    return self.name


class dbtoeic(models.Model):
    item = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False,default='')
    chinese = models.CharField(max_length=50, null=False)
    relate = models.CharField(max_length=50, blank=True , default='') 
    memo = models.CharField(max_length=200, blank=True , default='')
    level = models.IntegerField(blank=True, default=0)	
    toune = models.CharField(max_length=100, blank=True , default='')
    sound = models.CharField(max_length=200, blank=True , default='')
    wrong = models.IntegerField(blank=True, default=0)
    standard = models.IntegerField(blank=True, default=0)
    

    def __str__(self):
	    return self.name