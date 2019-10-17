from django.urls import path
from . import views

urlpatterns = [
    path('newreval/', views.new_reval, name = 'newreval'),


]