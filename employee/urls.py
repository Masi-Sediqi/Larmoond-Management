from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee_create/', views.employee_create, name='employee_create'),
    path('update/<int:employee_id>/', views.employee_update, name='employee_update'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('employee_detail/<int:employee_id>/', views.employee_detail, name='employee_detail'),
]