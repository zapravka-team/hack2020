from django.db import models

from .fields import MultiEmailField, MultiPhoneNumberField


class AnimalType(models.Model):
    name = models.CharField(max_length=120, null=False)


class AnimalShelter(models.Model):

    name = models.CharField(max_length=120, null=False)
    address = models.CharField(max_length=500, null=True)
    contact_emails = MultiEmailField(max_length=500, null=True)
    contact_phone_numbers = MultiPhoneNumberField(max_length=400, null=True)
    description = models.TextField(null=True)


class Animal(models.Model):

    # base information
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(null=True)
    bread = models.CharField(max_length=120, null=True)
    gender = models.CharField(max_length=120)
    birthdate = models.DateField(null=True)

    image = models.ImageField(upload_to='animal/img/', null=True)

    shelter = models.ForeignKey(AnimalShelter, on_delete=models.SET_NULL, null=True)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True)
