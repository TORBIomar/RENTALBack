# models.py
from django.db import models

class Utilisateur(models.Model):
    firebase_uid = models.CharField(max_length=128, unique=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    photo_url = models.URLField(blank=True, null=True)
    provider = models.CharField(max_length=50, default='password')
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    date_creation = models.DateTimeField(auto_now_add=True)
    derniere_modification = models.DateTimeField(auto_now=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'utilisateur'
        
    def __str__(self):
        return f"{self.nom} ({self.email})"

class Client(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='client')
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'client'
        
    def __str__(self):
        return f"Client: {self.utilisateur.nom}"

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    STATUT_CHOICES = (
        ('disponible', 'Disponible'),
        ('louee', 'Louée'),
        ('vendue', 'Vendue'),
        ('hors_service', 'Hors service'),
    )
    statut = models.CharField(max_length=15, choices=STATUT_CHOICES, default='disponible')
    categorie = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'voiture'
        
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"
        