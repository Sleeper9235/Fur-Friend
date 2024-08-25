from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal, AnimalList, AnimalShelter

# Create your views here.
# Home page - to display login/sign-up
class Home(LoginView):
    template_name = 'home.html'

# about the app 
def about(request):
    return render(request, 'about.html')

# profile once logged in
def profile(request):
    return render(request, 'animals/profile.html')

# main app page (all animals to be displayed and 'matching' happens here)
def animals_index(request):
    return render(request, 'animals/index.html')

# details for each animal 
def animal_details(request):
    return render(request, 'animals/details.html')

# to sign up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('group-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)