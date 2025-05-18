# firebase_auth.py
import firebase_admin
from firebase_admin import credentials, auth
from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.permissions import BasePermission

# Initialize Firebase Admin SDK (place this in your app's __init__.py or in this file)
try:
    cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
    firebase_admin.initialize_app(cred)
except ValueError:
    # App already exists
    pass

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        id_token = auth_header.split(' ').pop()
        if not id_token:
            return None

        try:
            # Verify the ID token
            decoded_token = auth.verify_id_token(id_token)
            firebase_uid = decoded_token['uid']
            
            # Return just the firebase_uid as the auth
            return (firebase_uid, None)
        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Token invalide: {str(e)}')

    def authenticate_header(self, request):
        return 'Bearer'

class IsFirebaseAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.auth)