from django.urls import path
from .views import listar_archivos, ejecutar_comando

urlpatterns = [
    path('listar/', listar_archivos, name='listar_archivos'),
    path('comando/', ejecutar_comando, name='ejecutar_comando'),
]
