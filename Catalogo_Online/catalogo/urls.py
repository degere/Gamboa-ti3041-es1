from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('producto/<int:id>/', views.detalle, name='detalle'),
]