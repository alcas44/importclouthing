from django import forms
from .models import Articulos


class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['codigo', 'referencia','descripcion', 'marca','precio_compra','precio_venta','descuento','imagen','existencia','usuario']

        widgets = { 
            'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Codigo','autofocus': True,'require':True}),
            'referencia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Referencia de Busqueda','require':True}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Descripcion','require':True}),
            'marca': forms.TextInput(attrs={'class': 'form-control','placeholder':'Marca','require':True}), 
            'precio_compra': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio Compra','require':True}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio Venta','require':True}),
            'descuento': forms.TextInput(attrs={'class': 'form-control','placeholder':'Descuento'}),
            'existencia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Existencia','require':True}),        
        }
        
