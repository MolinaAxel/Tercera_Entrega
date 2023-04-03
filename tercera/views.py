from django.shortcuts import render
from django.http import HttpResponse
from tercera.models import Materias, Personas, Compras
from tercera.forms import PersonasForm, MateriasForm,ComprasForm
from tercera.forms import buscarComprasForm, buscarMateriasForm, buscarPersonasForm
from django.views.generic.list import ListView



def mostrar_materias(request):
    materias = Materias.objects.all()
    context = {"materias":materias,
               "form": MateriasForm(),
    }
    return render(request, "tercera/Materias.html",context)

def crear_materias(request):
    f = MateriasForm(request.POST)

    context = {"form":f}

    if f.is_valid:
        Materias(Materia=f.data["Materia"],descripcion=f.data["descripcion"],estado=f.data["estado"]).save()
        context['form'] = MateriasForm()
    
    context["materias"] = Materias.objects.all()

    return render(request, "tercera/Materias.html", context)

def mostrar_personas(request):
    personas = Personas.objects.all()
    context = {"personas":personas,
               "form":PersonasForm(),
    }
    return render(request, "tercera/Personas.html", context)


def crear_persona(request):
    f = PersonasForm(request.POST)

    context = {"form":f}


    if f.is_valid:
        Personas(nombre=f.data["nombre"],apellido=f.data["apellido"]).save()
        context['form'] = PersonasForm()
    
    context["personas"] = Personas.objects.all()
    

    return render(request, "tercera/Personas.html", context)


def mostrar_compras(request):
    compras = Compras.objects.all()
    context = {"compras":compras,
               "form":ComprasForm()}
    return render(request, "tercera/Compras.html",context)

def crear_compras(request):
    f = ComprasForm(request.POST)

    context = {"form":f}


    if f.is_valid:
        Compras(producto=f.data["producto"],cantidad=f.data["cantidad"]).save()
        context['form'] = ComprasForm()
    
    context["compras"] = Compras.objects.all()
    

    return render(request, "tercera/Compras.html", context)

class buscarPersonas(ListView):
    model = Personas
    context_object_name = "personas"

    def get_queryset(self):
        f = buscarPersonasForm(self.request.GET)
        if f.is_valid:
            Personas.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Personas.objects.none()

class buscarMaterias(ListView):
    model = Materias
    context_object_name = "materias"

    def get_queryset(self):
        f = buscarMateriasForm(self.request.GET)
        if f.is_valid:
            Materias.objects.filter(nombre__icontains=f.data["criterio_materia"]).all()
        return Materias.objects.none()



class buscarCompras(ListView):
    model = Compras
    context_object_name = "compras"

    def get_queryset(self):
        f = buscarComprasForm(self.request.GET)
        if f.is_valid:
            Compras.objects.filter(nombre__icontains=f.data["criterio_producto"]).all()
        return Compras.objects.none()

