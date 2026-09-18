from django.shortcuts import render, redirect
from .forms import EmployeeForm,AttendanceForm,BankForm,SalaryForm
from .models import Employee,Attendance,Bank,Salary


def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employee_list.html',
        {'employees': employees}
    )


def employee_add(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employee_form.html',
        {'form': form}
    )
def employee_edit(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employee_form.html',
        {'form': form}
    )


def employee_delete(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(
        request,
        'employee_confirm_delete.html',
        {'employee': employee}
    )
def attendance_list(request):

    attendance = Attendance.objects.all().order_by('-date')

    return render(
        request,
        'attendance_list.html',
        {'attendance': attendance}
    )


def attendance_add(request):

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'attendance_form.html',
        {'form': form}
    )
def bank_list(request):

    banks = Bank.objects.all()

    return render(
        request,
        'bank_list.html',
        {'banks': banks}
    )


def bank_add(request):

    if request.method == 'POST':

        form = BankForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bank_list')

    else:
        form = BankForm()

    return render(
        request,
        'bank_form.html',
        {'form': form}
    )

def salary_add(request):
    if request.method == "POST":
        form = SalaryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('salary_list')

    else:
        form = SalaryForm()

    return render(request, 'salary_add.html', {'form': form})

def salary_list(request):

    salaries = Salary.objects.all()

    return render(
        request,
        'salary_list.html',
        {'salaries': salaries}
    )
def salary_edit(request, id):
    salary = Salary.objects.get(id=id)

    if request.method == "POST":
        form = SalaryForm(request.POST, instance=salary)

        if form.is_valid():
            salary = form.save()

            salary.net_salary = (
                salary.employee.salary
                + salary.incentive
                - salary.deduction
            )

            salary.save()

            return redirect('salary_list')

    else:
        form = SalaryForm(instance=salary)

    return render(request, 'salary_form.html', {'form': form})


def salary_delete(request, id):
    salary = Salary.objects.get(id=id)

    if request.method == "POST":
        salary.delete()
        return redirect('salary_list')

    return render(request, 'salary_delete.html', {'salary': salary})
from django.db.models import Sum
from .models import Employee, Attendance, Bank, Salary


def dashboard(request):

    total_employees = Employee.objects.count()
    total_attendance = Attendance.objects.count()
    total_bank = Bank.objects.count()
    total_salary = Salary.objects.count()

    total_payroll = Salary.objects.aggregate(
        total=Sum('net_salary')
    )['total'] or 0

    recent_salaries = Salary.objects.all().order_by('-id')[:5]

    context = {
        'total_employees': total_employees,
        'total_attendance': total_attendance,
        'total_bank': total_bank,
        'total_salary': total_salary,
        'total_payroll': total_payroll,
        'recent_salaries': recent_salaries,
    }

    return render(request, 'dashboard.html', context)