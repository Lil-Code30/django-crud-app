from django.shortcuts import render, redirect
from django.contrib import  messages
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

def add_records(request):
    if request.method  == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        telephone = request.POST['telephone']
        postal_code = request.POST['postalcode']
        position = request.POST['position']

        new_employee = Employee(firstname=firstname, lastname=lastname, email=email, telephone=telephone, postal_code=postal_code, position=position)
        new_employee.save()

        if new_employee.save:
            messages.success(request, 'New Employee added successfully')
            return redirect('index')
        else:
            messages.error(request, 'There was an error, Please Try Again')
            return redirect('add_employee')
