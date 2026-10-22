from django.shortcuts import render, redirect
from .models import Employee, Role, Department


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'all_emp.html', context)


def add_emp(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']

        # Department aur Role database se lena
        department = Department.objects.get(name=dept)
        role_obj = Role.objects.get(name=role)

        # Employee create karna
        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            dept=department,
            role=role_obj
        )

        return redirect('/all_emp')

    else:
        departments = Department.objects.all()
        roles = Role.objects.all()

        context = {
            'departments': departments,
            'roles': roles
        }

        return render(request, 'add_emp.html', context)


def remove_emp(request):
    if request.method == 'POST':

        emp_id = request.POST['emp_id']

        employee = Employee.objects.get(id=emp_id)

        employee.delete()

        return redirect('/all_emp')

    else:
        return render(request, 'remove_emp.html')


def filter_emp(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']

        employees = Employee.objects.all()

        if first_name:
            employees = employees.filter(
                first_name__icontains=first_name
            )

        if last_name:
            employees = employees.filter(
                last_name__icontains=last_name
            )

        if dept:
            employees = employees.filter(
                dept__name__icontains=dept
            )

        if role:
            employees = employees.filter(
                role__name__icontains=role
            )

        context = {
            'emps': employees
        }

        return render(request, 'all_emp.html', context)

    else:
        return render(request, 'filter_emp.html')
    
    
    