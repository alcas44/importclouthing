from django import forms
from .models import Articulos,Clientes,Envios


class ArticulosForm(forms.ModelForm):
   
    class Meta:
        model = Articulos
        fields = ['codigo','referencia','descripcion','color','marca','precio_compra','precio_venta','existencia','imagen']

        widgets = { 
            'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Codigo','autofocus': True,'require':True}),
            'referencia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Referencia de Busqueda','require':True}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Descripcion','require':True}),
            'color': forms.TextInput(attrs={'class': 'form-control','placeholder':'color','requiere':True}),
            'marca': forms.TextInput(attrs={'class': 'form-control','placeholder':'Marca','require':True}), 
            'precio_compra': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio Compra','require':True}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio Venta','require':True}),
            'existencia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Existencia','require':True}),
            'imagen': forms.FileInput(attrs={'class': 'form-control','require':False}),        
        }


class ClientesForm(forms.ModelForm):
    

    class Meta:
        model = Clientes
        fields = ['nit','negocio','nombres','apellidos','direccion','telefono','telefono2','correo']

        widgets = { 
            'nit': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nit','autofocus': True}),
            'negocio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Negocio','require':True}), 
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre','require':True}), 
            'apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos','require':True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Direccion','require':True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}),
            'telefono2': forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono2'}),
            'correo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo Electronico','require':True}),
                   
        }
        

TIPO_PAGO = [('','Elija Opcion de Envio'),('Pagado','Pagado'),('Pago Contra Entrega','Pago Contra Entrega')]
ESTADO = [('','Elija Estado del Envio'),('En Espera','En Espera de Envio'),('Enviado','Enviado'),('Cancelado','Cancelado')]


