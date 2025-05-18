# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Voiture, Client, Location
from .serializers import LocationSerializer
from datetime import datetime

@api_view(['POST'])
def rent_car(request):
    try:
        data = request.data
        voiture_id = data['voiture_id']
        client_id = data['client_id']
        date_debut = datetime.strptime(data['date_debut'], "%Y-%m-%d").date()
        date_fin = datetime.strptime(data['date_fin'], "%Y-%m-%d").date()

        voiture = Voiture.objects.get(id=voiture_id)
        if voiture.statut != 'disponible':
            return Response({'error': 'Voiture non disponible'}, status=400)

        days = (date_fin - date_debut).days
        cout_total = days * voiture.prix

        location = Location.objects.create(
            voiture=voiture,
            client_id=client_id,
            date_debut=date_debut,
            date_fin=date_fin,
            cout_total=cout_total,
        )

        voiture.statut = 'loué'
        voiture.save()

        return Response({'message': 'Location créée avec succès', 'location_id': location.id})
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)
