# firebase_auth/urls.py
from django.urls import path
from .views import SyncUserView

app_name = "firebase_auth"

urlpatterns = [
    # URL ends with a slash → sync-user/
    path('sync-user/', SyncUserView.as_view(), name='sync_user'),
]
