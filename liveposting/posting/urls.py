from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exotic/', views.exotic, name='exotic'),
    path('edit/<int:id>/', views.edit_species, name='edit_species'),
    path('delete/<int:id>/', views.delete_species, name='delete_species'),
   
]
