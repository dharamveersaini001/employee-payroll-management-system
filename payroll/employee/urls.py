from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('bank/', views.bank_list, name='bank_list'),
    path('bank/add/', views.bank_add, name='bank_add'),
    path('salary/add/', views.salary_add, name='salary_add'),
    path('salary/', views.salary_list, name='salary_list'),
    path('salary/edit/<int:id>/', views.salary_edit, name='salary_edit'),
    path('salary/delete/<int:id>/', views.salary_delete, name='salary_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
]