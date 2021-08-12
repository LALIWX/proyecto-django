from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return('created', 'updated', 'matricula', 'carrera', 'turno')
        else:
            return('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment', 'nombreMayus')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')
    list_per_page=3

    #Desplegar opciones avanzadas
    """ fieldsets = (
        (None, {
            'fields' : ('nombre',)
        }),
        ('Opciones avanzadas', {
            'classes' : ('collapse', 'wide', 'extrapretty'),
            'fields': ('matricula', 'carrera', 'turno', 'created')
        })
    )} """


    #Columna personalizada
    def nombreMayus (self, obj):
        return obj.nombre.upper()

    #Cambiar nombre de la columna
    nombreMayus.short_description='Nombre en mayusculas'

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
