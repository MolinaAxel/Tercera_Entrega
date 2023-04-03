from django import forms

class PersonasForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class MateriasForm(forms.Form):
    Materia = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=30)


class ComprasForm(forms.Form):
    producto = forms.CharField(max_length=15)
    cantidad = forms.IntegerField()

class buscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class buscarMateriasForm(forms.Form):
    criterio_materia = forms.CharField(max_length=100)

class buscarComprasForm(forms.Form):
    criterio_producto = forms.CharField(max_length=100)
