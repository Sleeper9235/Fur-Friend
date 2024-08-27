from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView
from django.db.models import Q


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
    #display user's animal shelter
    animal_shelter = AnimalShelter.objects.filter(user=request.user)
    #grabs user's animal list
    animal_list = AnimalList.objects.filter(user=request.user)
    
    return render(request, 'animals/profile.html', {'animal_shelter': animal_shelter, 'animal_list': animal_list})


# swiping page (all animals to be displayed and 'matching' happens here)
@login_required
def animals_index(request):
    all_animals = Animal.objects.filter(~Q(placeholder=" "))
    pks = []
    for animals in all_animals:
        pks.append(animals.pk)  
    
    print(pks)
    if pks:
        random_pk = random.choice(pks)
        animal = Animal.objects.get(pk=random_pk)
    else:
        animal = None
        
    animal_list = AnimalList.objects.filter(user=request.user)

    return render(request, 'animals/index.html', {'animal': animal, 'animal_list': animal_list})

# details for each animal 
@login_required
def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'animals/details.html', {'animal': animal})

@login_required
def add_animal_list(request, animal_id, list_id):
    animal_find = Animal.objects.get(pk=animal_id)
    animal_list = AnimalList.objects.get(pk=list_id)
    animal_list.animals.add(animal_find)
    return redirect('animal-index',)

@login_required
def animals_all(request):
    animals = Animal.objects.filter(user=request.user)
    return render(request, 'animals/yourAnimals.html', {'animals': animals})

@login_required
def your_animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'animals/your_animal_details.html', {'animal': animal})
    
@login_required
def toggle_shelter(request, animal_id):
    animal_shelter = AnimalShelter.objects.filter(user=request.user)
    animal = Animal.objects.get(pk=animal_id)
    print(animal.placeholder)
    if animal.placeholder == " ":
        for shelter in animal_shelter:
            shelter.animal.add(animal)
            animal.placeholder = shelter.id
    animal.save()
    return redirect('profile')

@login_required
def remove_animal(request, animal_id, animal_shelter_id):
    animal_shelter = AnimalShelter.objects.get(pk=animal_shelter_id)
    animal = Animal.objects.get(pk=animal_id)
    if int(animal.placeholder) == int(animal_shelter_id):
        animal.placeholder = " "
        animal.save()
    animal_shelter.animal.remove(animal)
    return redirect('profile')

@login_required
def animal_list_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'animals/animal_list_details.html', {'animal': animal})

@login_required
def list_remove_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    animal_list = AnimalList.objects.filter(user=request.user)
    for list in animal_list:
        list.animals.remove(animal)
    return redirect('profile')

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
    fields = ['name', 'age', 'likes', 'personality', 'type', 'breed', 'gender', 'fixed', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            return form_class(**self.get_form_kwargs())
        
class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['name', 'age', 'likes', 'personality', 'type', 'breed', 'gender', 'fixed', 'image']

class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = '/profile'
    
class AnimalShelterCreate(LoginRequiredMixin, CreateView):
    model = AnimalShelter
    fields = ['name']
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class AnimalShelterUpdate(LoginRequiredMixin, UpdateView):
    model = AnimalShelter
    fields = ['name']
    
class AnimalShelterDelete(LoginRequiredMixin, DeleteView):
    model = AnimalShelter
    success_url = '/profile/'
    
    
class AnimalListCreate(LoginRequiredMixin, CreateView):
    model = AnimalList
    fields = ['name']
    
class AnimalListUpdate(LoginRequiredMixin, UpdateView):
    model = AnimalList
    fields = ['name']
    
class AnimalListDelete(LoginRequiredMixin, DeleteView):
    model = AnimalList
    success_url = '/profile/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    