from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal, AnimalList, AnimalShelter

import random

# Create your views here.
# Home page - to display login/sign-up
class Home(LoginView):
    template_name = 'home.html'

# about the app 
def about(request):
    return render(request, 'about.html')

# profile once logged in
@login_required
def profile(request):
    animal_shelter = AnimalShelter.objects.filter(user=request.user)
    my_animals = []
    allAnimals = Animal.objects.all()
    for animal in allAnimals:
        print(animal.animal_shelter)
        if animal.animal_shelter in animal_shelter:
            my_animals.append(animal)
    
    return render(request, 'animals/profile.html', {'animal_shelter': animal_shelter, 'my_animals': my_animals})


# swiping page (all animals to be displayed and 'matching' happens here)
@login_required
def animals_index(request):
    animals = Animal.objects.all()
    for animal in animals:
        random_number = random.sample(range(1, (len(animals) + 1)), 1)
        animal.placeholder = random_number

    
    return render(request, 'animals/index.html', {'animals': animals})

# details for each animal 
@login_required
def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'animals/details.html', {'animal': animal})

# to sign up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # form.instance is the cat
        return super().form_valid(form)
    
class AnimalShelterCreate(LoginRequiredMixin, CreateView):
    model = AnimalShelter
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # form.instance is the cat
        return super().form_valid(form)
    
    