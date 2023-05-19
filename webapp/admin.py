from django.contrib import admin
from .models import Usuario, Obra, Avaliacao, Lista, Feed, Seguidores


admin.site.register(Usuario)
admin.site.register(Obra)
admin.site.register(Avaliacao)
admin.site.register(Lista)
admin.site.register(Feed)
admin.site.register(Seguidores)