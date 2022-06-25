from django import forms
from .models import Articulos,Clientes


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



TIPO = [('Minorista','Minorista'),('Mayorista','Mayorista')]

class ClientesForm(forms.ModelForm):
    

    class Meta:
        model = Clientes
        fields = ['codigo', 'nit','tipo', 'nombres','apellidos','direccion','telefono','correo','fecha_nac','cuenta','usuario']

        widgets = { 
            'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Codigo','autofocus': True,'require':True}),
            'nit': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nit','require':True}),
            'tipo': forms.Select(attrs={'class':'form-control'},choices=TIPO),
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre','require':True}), 
            'apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos','require':True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Direccion','require':True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}),
            'correo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo Electronico'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'cuenta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Q.0.00','readonly':True,'default':0.00}),        
        }
        
