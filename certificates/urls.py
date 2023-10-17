from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
]
