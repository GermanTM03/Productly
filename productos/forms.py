from . import models
from django.forms import ModelForm
 
 
class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre','cantidad','puntaje','categoria']