# RENTAL/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # if React is calling /api/auth/sync-user/, you must mount it at 'api/auth/'
    path('api/auth/', include('firebase_auth.urls', namespace='firebase_auth')),
     
]
