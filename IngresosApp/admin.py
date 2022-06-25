from django.contrib import admin
from IngresosApp.models import Articulos

class ArticuloAdmin(admin.ModelAdmin):
    list_display= ('codigo','referencia','imagen')




admin.site.register(Articulos,ArticuloAdmin)    

