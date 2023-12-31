from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id','nombre','cantidad','puntaje','creado_en')

admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Producto,ProductoAdmin)