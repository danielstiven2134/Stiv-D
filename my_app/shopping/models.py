from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad}'

    class Meta:
        verbose_name_plural = "Inventarios"


class Factura(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.numero_factura

    class Meta:
        verbose_name_plural = "Facturas"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.factura.numero_factura} - {self.producto.nombre}'

    class Meta:
        verbose_name_plural = "Detalles de Factura"


class Devolucion(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    motivo = models.TextField()
    fecha_devolucion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Devolución {self.id} - {self.producto.nombre}'

    class Meta:
        verbose_name_plural = "Devoluciones"
