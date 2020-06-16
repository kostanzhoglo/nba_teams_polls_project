from django.urls import path

from . import views

# namespace
app_name = 'polls'
urlpatterns = [
    # next line is creating a route
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results')
]