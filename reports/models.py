from django.db import models
from mir1.models import users
# Create your models here.

class benefits(models.Model):

    state_idb = models.CharField(max_length=2,primary_key= True)
    state_nameb = models.CharField(max_length= 20)
    target = models.CharField(max_length=10)
    profit_amt = models.CharField(max_length=20)

class water(models.Model):
    state_idw = models.CharField(max_length=2,primary_key= True)
    state_namew = models.CharField(max_length= 20)
    source = models.CharField(max_length=20)
    litres_prov = models.IntegerField()
    litres_benefit = models.IntegerField()

class state(models.Model):
    state_ids = models.CharField(max_length=2,primary_key= True)
    state_names = models.CharField(max_length= 20)
    cum_budget = models.CharField(max_length=7)
    achieved = models.CharField(max_length=7)

class area(models.Model):
    state_ida = models.CharField(max_length=2,primary_key= True)
    state_namea = models.CharField(max_length= 20)
    area_target = models.CharField(max_length=7)
    area_saved = models.CharField(max_length=7)




