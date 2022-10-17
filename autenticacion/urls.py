
from django.urls import path
from app import views
from django.conf.urls.static import static
from .views import VRegistro

urlpatterns = [
   
    path('',VRegistro.as_view(),name="Autenticacion"),  
]


