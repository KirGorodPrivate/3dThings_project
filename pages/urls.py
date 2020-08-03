from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('materials', views.materials, name='materials'),
    path('design', views.design, name='design'),
]