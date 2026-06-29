from django.contrib import admin
from .models import Vehicle, VehicleImage

class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 5

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        'marque',
        'modele',
        'annee',
        'prix',
        'disponible'
    )
    
    inlines = [VehicleImageInline]