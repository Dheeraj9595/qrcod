# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # Example URL pattern
    path('generate_qr/', views.generate_qr, name='generate_qr'),  # Example URL pattern for generating QR code
    # Add more URL patterns as needed
]
