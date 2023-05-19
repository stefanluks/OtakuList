from django.contrib import admin
from django.urls import path, include
from webapp.views import Home, Perfil, ListaView, OpenNews

urlpatterns = [
    path('', Home, name="Home"),
    path('admin/', admin.site.urls),
    path('Perfil/<str:user>/', Perfil, name="Perfil"),
    path('Lista/<int:id>', ListaView, name="Lista"),
    path('OpenNews/<int:idFeed>', OpenNews, name="OpenNews"),
    path('u/',include('django.contrib.auth.urls')),
]
