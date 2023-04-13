
# Create your models here.
from django.db import models

class Car(models.Model):
    YEAR_CHOICES = [(i, i) for i in range(1950, 2031)]

    year = models.IntegerField(choices=YEAR_CHOICES)
    present_price = models.FloatField()
    kms_driven = models.IntegerField()
    owner = models.IntegerField()
    fuel_type_petrol = models.BooleanField()
    fuel_type_diesel = models.BooleanField()
    seller_type_individual = models.BooleanField()
    transmission_manual = models.BooleanField()