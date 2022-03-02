# Пример связывания через интерфейсы

from abc import ABC, abstractmethod

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        for employee in employees:
            print(employee.id, employee.name)
            print(employee.calculate_payroll())
            print()


class Employee(ABC):
    def __init__(self, id, name):
       self.id = id
       self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 100


s_employee = SalaryEmployee(1, 'Ivan', 30000)
h_employee = HourlyEmployee(2, 'Petr', 40, 1500)
c_employee = CommissionEmployee(3, 'Sidr', 100000, 250000)
d_employee = DisgruntledEmployee(4, 'Jane')

payroll = PayrollSystem()
payroll.calculate_payroll([
    s_employee,
    h_employee,
    c_employee,
    d_employee
])