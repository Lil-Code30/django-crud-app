from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('register/', views.add_records, name='add_records'),
]
