from django.urls import path
from adotar.views import listar_pets, solicitar_adocao


urlpatterns = [
    path('', listar_pets, name='listar_pets'),
    path('solicitar_adocao/<int:id>/', solicitar_adocao, name='solicitar_adocao'),
] 
