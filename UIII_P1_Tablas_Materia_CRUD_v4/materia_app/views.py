from django.shortcuts import render, redirect
from .models import Materia
# Create your views here.
def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,'gestionarMaterias.html',{"mismaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcredito"]

    guardarmateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    ) 
    return redirect ("/")

def seleccionarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarMateria.html",{"mismaterias":materia})


def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcredito"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()
    return redirect("/") #dsf


def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    return redirect("/") #asdsda
