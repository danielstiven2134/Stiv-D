from django import forms
from .models import Factura, DetalleFactura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['numero_factura', 'cliente']


class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ['producto', 'cantidad', 'precio_unitario']
