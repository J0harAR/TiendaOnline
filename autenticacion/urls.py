
from django.urls import path
from app import views
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
    path('',views.autenticacion,name="Autenticacion"),  
]


