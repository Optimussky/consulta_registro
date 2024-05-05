from django.contrib import admin
from .models import CatalogoDelito, CatalogoPersona, RegistroDelitos
# Register your models here.

#class CatalogoDelito(admin.ModelAdmin):
    #list_display = ('delito',)
	#list_display =('id','delito')
	# list_filter = ('delito')
	# search_fields = ('delito','fechaCreacion')


#class CatalogoPersona(admin.ModelAdmin):
    #list_display = ('tipo_persona',)
	#list_display =('id','tipo_persona','status')
	# list_filter = ('tipo_persona')
	# search_fields = ('tipo_persona','fechaCreacion')


#class RegistroDelitos(admin.ModelAdmin):
    #list_display = ('registro',)
	#list_display =('id','registro','fechaCreacion','id_catalogoPersona')
	# list_filter = ('registro')
	# search_fields = ('fechaCreacion')


admin.site.register(CatalogoDelito)
admin.site.register(CatalogoPersona)
admin.site.register(RegistroDelitos)
