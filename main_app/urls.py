from django.urls import path
from . import views 

urlpatterns = [
    # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('animals/', views.animals_index, name='animal-index'),
    path('animals/yourAnimals/', views.animals_all, name="your-animals"),
    path('animals/<int:animal_id>/', views.animal_details, name='animal-details'),
    path('animals/yourAnimals/<int:animal_id>/', views.your_animal_details, name="your-animal-details"),
    path('animals/<int:animal_id>/listDetails', views.animal_list_details, name="animal-list-details"),
    path('animals/<int:animal_id>/listDetails/delete', views.list_remove_animal, name="list-remove-animal"),
    path('animals/yourAnimals/<int:animal_id>/toggleShelter', views.toggle_shelter, name="toggle-shelter"),
    path('animals/yourAnimals/<int:animal_id>/removeAnimal/<int:animal_shelter_id>', views.remove_animal, name="remove-animal"),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal-update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal-delete'),
    path('animalShelter/Create/', views.AnimalShelterCreate.as_view(), name='animal-shelter-create'),
    path('animalShelter/<int:pk>/update/', views.AnimalShelterUpdate.as_view(), name='animal-shelter-update'),
    path('animalShelter/<int:pk>/delete/', views.AnimalShelterDelete.as_view(), name='animal-shelter-delete'),
    path('animalList/Create/', views.AnimalListCreate.as_view(), name="animal-list-create"),
    path('animalList/<int:pk>/update/', views.AnimalListUpdate.as_view(), name='animal-list-update'),
    path('animalList/<int:pk>/delete/', views.AnimalListDelete.as_view(), name='animal-list-delete'),
    path('animals/<int:animal_id>/addAnimalList/<int:list_id>', views.add_animal_list, name="add-animal-list"),

]


