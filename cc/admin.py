from django.contrib import admin

# Register your models here.
from .models import Categoria, Icono, RedSocial, Empresa, EmpresaRedSocial, Producto, CaracteristicaProducto, Servicio, Testimonio, MensajeContacto

admin.site.register(Categoria)
admin.site.register(Icono)
admin.site.register(RedSocial)
admin.site.register(Empresa)
admin.site.register(EmpresaRedSocial)
admin.site.register(Producto)
admin.site.register(CaracteristicaProducto)
admin.site.register(Servicio)
admin.site.register(Testimonio)
admin.site.register(MensajeContacto)