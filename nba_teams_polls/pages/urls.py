from django.urls import path

from . import views

urlpatterns = [
    # next line is creating a route
    path('', views.index, name='index')
]