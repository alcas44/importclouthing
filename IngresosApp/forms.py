from django import forms
from .models import Articulos,Clientes,Envios


class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['codigo', 'referencia','descripcion', 'marca','precio_compra','precio_venta','descuento','existencia','imagen']

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
        





TIPO_PAGO = [('','Elija Opcion de Envio'),('Pagado','Pagado'),('Pago Contra Entrega','Pago Contra Entrega')]
ESTADO = [('','Elija Estado del Envio'),('En Espera','En Espera de Envio'),('Enviado','Enviado'),('Cancelado','Cancelado')]

class EnviosForm(forms.ModelForm):
    

    class Meta:
        model = Envios
        fields = ['codigo','tipo','remitente','destinatario','direccion','telefono','estado','monto','guia','observacion']

        widgets = { 
            'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Codigo Envio','autofocus': True,'require':True}),
            'tipo': forms.Select(attrs={'class':'form-control'},choices=TIPO_PAGO),
            'remitente': forms.TextInput(attrs={'class': 'form-control','placeholder':'Remitente','require':True}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control','placeholder':'Destinatario','require':True}), 
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Direccion','require':True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}), 
            'estado': forms.Select(attrs={'class':'form-control'},choices=ESTADO),
            'monto': forms.TextInput(attrs={'class': 'form-control','placeholder':'Q.0.00','required':True}),
            'guia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Guia de Envio Para Rastreo'}), 
            'observacion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Observaciones o Detalles de Entrega'}),        
        }
                
