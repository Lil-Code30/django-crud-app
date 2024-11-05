from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('delete-employee/<int:id>', views.delete_employee, name='delete_employee'),
    path('update-employee/<int:id>', views.update_employee, name='update_employee'),  
    path('register/', views.add_records, name='add_records'),
    path('update/', views.update_records, name='update_records'),
]
