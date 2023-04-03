from django.contrib import admin
from django.urls import path
from tercera.views import mostrar_materias, mostrar_personas, crear_persona,mostrar_compras,crear_materias
from tercera.views import crear_compras, buscarPersonas, buscarMaterias, buscarCompras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materias', mostrar_materias, name="materias"),
    path('materias/create',crear_materias, name="materias-create"),
    path('materias/list', buscarMaterias.as_view(), name="materias-list"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('personas/list', buscarPersonas.as_view(), name="personas-list"),
    path('compras', mostrar_compras, name="compras"),
    path('compras/create', crear_compras, name="compras-create"),
    path('compras/list', buscarCompras.as_view(), name="compras-list"),
]
