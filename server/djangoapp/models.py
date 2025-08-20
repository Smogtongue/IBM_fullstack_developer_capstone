# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Meta:
    ordering = ['-year', 'name']


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('CROSSOVER', 'Crossover'),
        ('EV', 'Electric Vehicle'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(
        default=now().year,
        validators=[
            MaxValueValidator(now().year),
            MinValueValidator(2015)
        ]
    )

    CAR_CONDITIONS = [
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('EV', 'Electric'),
    ]
    condition = models.CharField(max_length=10, choices=CAR_CONDITIONS,
                                 default='NEW')

    color = models.CharField(max_length=30, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)

    def __str__(self):
        return self.name
