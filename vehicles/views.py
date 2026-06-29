from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from .forms import SearchForm
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):

    vehicles = Vehicle.objects.filter(disponible=True)

    query = request.GET.get('query', '').strip()
    type_vehicule = request.GET.get('type_vehicule', '')
    carburant = request.GET.get('carburant', '')
    transmission = request.GET.get('transmission', '')
    prix_min = request.GET.get('prix_min', '')
    prix_max = request.GET.get('prix_max', '')
    annee_min = request.GET.get('annee_min', '')
    km_max = request.GET.get('km_max', '')
    sort = request.GET.get('sort', '')

    if query:
        vehicles = vehicles.filter(
            Q(marque__icontains=query) |
            Q(modele__icontains=query)
        )

    if type_vehicule:
        vehicles = vehicles.filter(type_vehicule=type_vehicule)

    if carburant:
        vehicles = vehicles.filter(carburant=carburant)

    if transmission:
        vehicles = vehicles.filter(transmission=transmission)

    if prix_min:
        vehicles = vehicles.filter(prix__gte=prix_min)

    if prix_max:
        vehicles = vehicles.filter(prix__lte=prix_max)

    if annee_min and annee_min.isdigit():
        vehicles = vehicles.filter(annee__gte=int(annee_min))

    if km_max:
        vehicles = vehicles.filter(kilometrage__lte=km_max)

    # Tri
    if sort == 'prix_asc':
        vehicles = vehicles.order_by('prix')
    elif sort == 'prix_desc':
        vehicles = vehicles.order_by('-prix')
    elif sort == 'annee_desc':
        vehicles = vehicles.order_by('-annee')
    elif sort == 'km_asc':
        vehicles = vehicles.order_by('kilometrage')

    paginator = Paginator(vehicles, 9)
    page_number = request.GET.get('page')
    vehicles = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'vehicles': vehicles,
        'query': query,
    })
    
def detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'detail.html', {
        'vehicle': vehicle
    })
    
def search(request):

    # filtres
    vehicles = Vehicle.objects.filter(disponible=True)
    type_vehicule = request.GET.get('type_vehicule', '')


    query = request.GET.get('query', '').strip()
    carburant = request.GET.get('carburant', '').strip()
    transmission = request.GET.get('transmission', '').strip()
    prix_max = request.GET.get('prix_max', '').strip()
    annee_min = request.GET.get('annee_min', '').strip()

    print("GET DATA:", request.GET)

    # Recherche texte
    if query:
        vehicles = vehicles.filter(
            Q(marque__icontains=query) |
            Q(modele__icontains=query)
        )

    # Type de véhicule
    if type_vehicule:
        vehicles = vehicles.filter(
            type_vehicule=type_vehicule
        )

    # carburant
    if carburant:
        vehicles = vehicles.filter(carburant=carburant)

    # transmission
    if transmission:
        vehicles = vehicles.filter(transmission=transmission)

    # prix max
    if prix_max:
        vehicles = vehicles.filter(prix__lte=prix_max)

    # année min (IMPORTANT FIX)
    if annee_min and annee_min.isdigit():
        vehicles = vehicles.filter(annee__gte=int(annee_min))
    sort = request.GET.get('sort', '')
    
    if sort == 'prix_asc':
        vehicles = vehicles.order_by('prix')
    elif sort == 'prix_desc':
        vehicles = vehicles.order_by('-prix')
    elif sort == 'annee_desc':
        vehicles = vehicles.order_by('-annee')
    elif sort == 'km_asc':
        vehicles = vehicles.order_by('kilometrage')
        
    prix_min = request.GET.get('prix_min', '')
    prix_max = request.GET.get('prix_max', '')

    if prix_min:
        vehicles = vehicles.filter(prix__gte=prix_min)

    if prix_max:
        vehicles = vehicles.filter(prix__lte=prix_max)

    km_max = request.GET.get('km_max', '')

    if km_max:
        vehicles = vehicles.filter(kilometrage__lte=km_max)
  
    paginator = Paginator(vehicles, 9)
    page_number = request.GET.get('page')
    vehicles = paginator.get_page(page_number)

    return render(request, 'search.html', {
        'vehicles': vehicles,
        'query': query,
        'carburant': carburant,
        'transmission': transmission,
        'prix_max': prix_max,
        'annee_min': annee_min,
    })
