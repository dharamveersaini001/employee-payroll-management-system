from django.db import models


class Employee(models.Model):

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    present = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.date}"


class Bank(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='bank_details'
    )

    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee.name} - {self.bank_name}"


class Salary(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='salary_records'
    )

    month = models.CharField(
    max_length=20,
    default=""
)

    incentive = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deduction = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):

        self.net_salary = (
            self.employee.salary
            + self.incentive
            - self.deduction
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.month}"