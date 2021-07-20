from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car_Brands(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car_Models(models.Model):
    brand = models.ForeignKey(Car_Brands, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HomeLoan(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    purchase_price = models.BigIntegerField(null=True)
    down_payment = models.IntegerField(null=True)
    desired_loan = models.BigIntegerField(null=True)

class CarLoan(models.Model):
    car_brands = models.ForeignKey(Car_Brands, on_delete=models.SET_NULL, null=True)
    car_models = models.ForeignKey(Car_Models, on_delete=models.SET_NULL, null=True)
    purchase_price = models.BigIntegerField()
    down_payment = models.IntegerField()
    desired_loan = models.BigIntegerField()

