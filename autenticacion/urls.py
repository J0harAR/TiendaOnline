
from django.urls import path
from app import views
from django.conf.urls.static import static
from .views import VRegistro,cerrar_sesion

urlpatterns = [
   
    path('',VRegistro.as_view(),name="Autenticacion"),  
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),  
]


