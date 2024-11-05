from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'telephone', 'postal_code', 'position', 'created_at')

admin.site.register(Employee,  EmployeeAdmin)
