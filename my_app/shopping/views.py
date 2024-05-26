from django.shortcuts import render, redirect
from .forms import FacturaForm, DetalleFacturaForm
from .models import Factura, DetalleFactura


def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        detalle_form = DetalleFacturaForm(request.POST)

        if factura_form.is_valid() and detalle_form.is_valid():
            factura = factura_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.factura = factura
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario
            detalle.save()
            factura.total += float(detalle.subtotal)
            factura.save()
            return redirect('factura_detalle', factura_id=factura.id)
    else:
        factura_form = FacturaForm()
        detalle_form = DetalleFacturaForm()

    return render(request, 'shopping/crear_factura.html', {
        'factura_form': factura_form,
        'detalle_form': detalle_form,
    })
