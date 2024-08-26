from django.urls import path
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('animals/', views.animals_index, name='animal-index'),
    path('animals/<int:animal_id>/', views.animal_details, name='animal-details'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('animals/animalShelterCreate/', views.AnimalShelterCreate.as_view(), name='animal-shelter-create')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


