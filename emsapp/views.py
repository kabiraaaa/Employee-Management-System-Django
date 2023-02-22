from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

def homepage(request):
    employees = Employee.objects.all
    return render(request, 'home.html', {'employees' : employees})

def demo(request):
    return HttpResponse('demo Page')

def employee_details(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return HttpResponse('Employee Not Found')
    return render(request, 'employee_detail.html', {'employee': employee})