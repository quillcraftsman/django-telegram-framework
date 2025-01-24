from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('start/', views.start_command_view, name='start'),
    path('help/', views.help_command_view, name='help'),
    path('links/', views.links_view, name='links'),
]
