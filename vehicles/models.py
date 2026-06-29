from django.db import models



class Vehicle(models.Model):
    TYPE_CHOICES = [
    ('neuve', 'Voiture neuve'),
    ('moins3ans', 'Voiture moins de 3 ans'),
    ('occasion', 'Voiture d\'occasion'),
    ]

    type_vehicule = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='moins3ans'
    )
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    kilometrage = models.IntegerField()
    
    carburant = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True
    )
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"Image - {self.vehicle}"