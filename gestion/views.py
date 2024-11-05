from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    employees =  Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)

def add_employee(request):
    return  render(request, 'add_employee.html')

