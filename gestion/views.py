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
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, 'Emloyee deleted successfully')
    return redirect('index')

def update_employee(request, id):
    employee = Employee.objects.get(id=id)

    return  render(request, 'update_employee.html', {'employee':employee})

def update_records(request, id):
    if request.method  == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        telephone = request.POST['telephone']
        postal_code = request.POST['postalcode']
        position = request.POST['position']

        employee = Employee.objects.get(id=id)

        employee.firstname = firstname
        employee.lastname = lastname
        employee.email = email
        employee.telephone = telephone
        employee.postal_code = postal_code
        employee.position = position

        employee.save()

        if employee.save:
            messages.success(request, 'Employee\'s Informations updated successfully')
            return redirect('index')
        else:
            messages.error(request, 'There was an error, Please Try Again')
            return redirect('update_employee')