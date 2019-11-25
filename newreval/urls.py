from django.urls import path
from . import views

urlpatterns = [
    path('head/', views.new_reval_head, name='newrevalhead'),
    path('tail/', views.new_reval, name = 'newreval'),
    path('result/', views.result, name='result'),

]