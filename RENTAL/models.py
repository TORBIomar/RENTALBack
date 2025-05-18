# models.py
from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=[('disponible','disponible'),('loué','loué'),('maintenance','maintenance'),('vendu','vendu')], default='disponible')

class Client(models.Model):
    utilisateur = models.OneToOneField('Utilisateur', on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

class Location(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    cout_total = models.DecimalField(max_digits=10, decimal_places=2)
    statut_location = models.CharField(max_length=20, choices=[('réservé','réservé'),('en cours','en cours'),('terminé','terminé'),('annulé','annulé')], default='réservé')
    date_reservation = models.DateTimeField(auto_now_add=True)
