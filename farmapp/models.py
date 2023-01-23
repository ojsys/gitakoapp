from django.db import models

# Create your models here.

class FarmBlock(models.Model):
    blockname = models.CharField(max_length=60)
    blocksize = models.IntegerField()
    crop = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    numberofridges = models.IntegerField()
    blockmanager = models.CharField(max_length=100)
    obstacles = models.CharField(max_length=100)
    sizeofobstacles = models.FloatField()
    remark = models.TextField()

    def __str__(self):
        return self.blockname



class FarmBudget(models.Model):
    farmname = models.CharField(max_length=100, blank=True)
    blocks = models.IntegerField()
    crop = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    hectares = models.IntegerField()
    cropseason = models.CharField(max_length=100)
    particulars = models.CharField(max_length=200)
    productbrand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    units = models.IntegerField()
    rates = models.FloatField()
    totalcost = models.FloatField()

    def __str__(self):
        return self.farmname



class CropCalendar(models.Model):
    activity = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.activity

