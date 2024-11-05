from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('delete-employee/<int:id>', views.delete_employee, name='delete_employee'),
    path('register/', views.add_records, name='add_records'),
]
