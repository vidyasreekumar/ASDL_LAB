from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_reval_head, name='newrevalhead'),
    path('newreval/', views.new_reval, name = 'newreval'),


]