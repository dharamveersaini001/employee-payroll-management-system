from django import forms
from .models import Employee,Attendance,Bank,Salary


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'employee_id',
            'name',
            'email',
            'phone',
            'address',
            'department',
            'designation',
            'joining_date',
            'salary',
        ]

        widgets = {
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = [
            'employee',
            'date',
            'present',
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = [
            'employee',
            'bank_name',
            'branch',
            'account_type',
            'account_number',
        ]

from django import forms
from .models import Salary


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['employee', 'incentive', 'deduction']