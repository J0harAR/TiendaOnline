from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.
class VRegistro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})
        
    def post(self,request):#Envio de informacion del formulario
         form=UserCreationForm(request.POST)#almacenamos contrase;a y usuario       
         if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect('Home')
         else:
            for msg in form.error_messages:
              messages.error(request,form.error_messages[msg])      
         return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect ('Home')