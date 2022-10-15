from django.shortcuts import render
from blog.models import post,Categoria

# Create your views here.
def blog(request):
    posts=post.objects.all()
    categorias=Categoria.objects.all()
    return render(request,'blog/blog.html',{"posts":posts,"categoriasFiltro":categorias})
def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    categorias=Categoria.objects.all()
    posts=post.objects.filter(categorias=categoria)
    return render(request,"blog/categorias.html",{"categoria":categoria,"posts":posts,"categoriasFiltro":categorias})
