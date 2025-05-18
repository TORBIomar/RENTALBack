# firebase_auth/views.py
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth as firebase_auth
from .models import Utilisateur
    

class SyncUserView(APIView):
    authentication_classes = []  # we verify manually below
    permission_classes     = []  # allow all (we handle auth ourselves)

    def post(self, request):
        # 1) Extract token from Authorization header
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return Response({'detail': 'Missing or malformed Authorization header'},
                            status=status.HTTP_401_UNAUTHORIZED)

        id_token = auth_header.split('Bearer ')[1]

        # 2) Verify with Firebase Admin SDK
        try:
            decoded = firebase_auth.verify_id_token(id_token)
        except Exception:
            return Response({'detail': 'Invalid Firebase ID token'},
                            status=status.HTTP_401_UNAUTHORIZED)

        uid = decoded['uid']

        # 3) Pull fields from incoming JSON
        data     = request.data
        email    = data.get('email')
        nom      = data.get('nom', '')          # must match React payload key
        photo    = data.get('photo_url')
        provider = data.get('provider', 'password')

        # 4) Upsert into your MySQL table
        user, created = Utilisateur.objects.update_or_create(
            firebase_uid=uid,
            defaults={
                'email':     email,
                'nom':       nom,
                'photo_url': photo,
                'provider':  provider,
            }
        )

        # 5) Return the new/updated user record
        return Response({
            'id':           user.id,
            'firebase_uid': user.firebase_uid,
            'email':        user.email,
            'nom':          user.nom,
            'photo_url':    user.photo_url,
            'provider':     user.provider,
            'created':      created
        }, status=(status.HTTP_201_CREATED if created else status.HTTP_200_OK))
# firebase_auth/urls.py
# firebase_auth/views.py

   