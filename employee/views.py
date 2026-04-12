from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def employee_create(request):
    employee_records = Employee.objects.all().order_by('-id')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully 👤")
            return redirect('employee:employee_create')
        else:
            messages.error(request, "Failed to add employee ❌")
    else:
        form = EmployeeForm()

    context = {
        'employee_form': form,
        'employee_records': employee_records
    }

    return render(request, 'employee/employee_form.html', context)


def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully ✏️")
        else:
            messages.error(request, "Failed to update employee ❌")

    return redirect('employee:employee_create')


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee_name = f"{employee.first_name} {employee.last_name}".strip()
        employee.delete()
        messages.success(request, f"Employee '{employee_name}' deleted successfully 🗑️")
    else:
        messages.warning(request, "Invalid delete request ⚠️")

    return redirect('employee:employee_create')


def employee_detail(request, employee_id):
    # Get the employee object
    employee = get_object_or_404(Employee, id=employee_id)
    
    # Get projects where this employee is a member
    assigned_projects = employee.assigned_projects.all()  # Using the related_name from Project model
    

    # Combine all projects (unique)
    all_projects = assigned_projects
    all_projects = all_projects.distinct().order_by('-created_at')
    
    # Calculate statistics
    total_projects = all_projects.count()
    active_projects = all_projects.filter(status='in_progress').count()
    completed_projects = all_projects.filter(status='completed').count()
    
    context = {
        'employee': employee,
        'projects': all_projects,
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
    }
    return render(request, 'employee/employee_detail.html', context)