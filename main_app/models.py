from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile')
    
class Interest(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile')

FIXING_CHOICES = (('Spayed', 'Spayed'), ('Neutered', 'Neutered'), ('Not Applicable', 'Not Applicable'))
GENDER_CHOICES = (('Female', 'Female'), ('Male', 'Male'))
TYPE_CHOICES = (('Dog', 'Dog'), ('Cat', 'Cat'))

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', default="media/paw-print-heart-connected_78370-3265.avif", null=True, blank=True)
    placeholder = models.CharField(max_length=100, default=" ", editable=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None)
    age = models.IntegerField()
    likes = models.ManyToManyField(Interest, blank=True)
    personality = models.ManyToManyField(Trait, blank=True)
    breed = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=None)
    fixed = models.CharField(max_length=14, choices=FIXING_CHOICES, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def __str__(self):
        return self.name
    
        
class AnimalList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animal, blank=True)
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def __str__(self):
        return self.name
    
class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default=" ")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed. Do not include area code.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ManyToManyField(Animal, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile')