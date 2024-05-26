from django.contrib import admin
from .models import Producto, Inventario, Factura, DetalleFactura, Devolucion


admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Devolucion)
