from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_app/static/images', null=True, blank=True)
    placeholder = models.CharField(max_length=100, default=" ", editable=False)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    breed = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class AnimalList(models.Model):
    name = models.CharField(max_length=100)
    
