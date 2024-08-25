from django.contrib import admin
from .models import Animal, AnimalList, AnimalShelter

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
class AnimalShelterAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
class AnimalListAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Animal, AnimalAdmin,)
admin.site.register(AnimalShelter, AnimalShelterAdmin)
admin.site.register(AnimalList, AnimalListAdmin)
