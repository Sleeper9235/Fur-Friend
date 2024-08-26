from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile')
    
class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile')
    
class AnimalList(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

FIXING_CHOICES = (('spayed', 'SPAYED'), ('neutered', 'NEUTERED'))


class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/uploads/', null=True, blank=True)
    placeholder = models.CharField(max_length=100, default=" ", editable=False)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    personality = models.ManyToManyField(Trait)
    breed = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    fixed = models.CharField(max_length=8, choices=FIXING_CHOICES, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_shelter = models.ForeignKey(AnimalShelter, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def __str__(self):
        return self.name
