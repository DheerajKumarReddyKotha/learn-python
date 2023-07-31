from employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employee's:")

        for emp in self.employees:
            print(emp.fname, emp.lname)

    def pay_employees(self):
        for emp in self.employees:
            print("Paying Employee's:")
            print("Pay check for:", emp.fname, emp.lname)
            print(f"Amount:${emp.calculate_paycheck():,.2f}")


def main():
    my_company = Company()

    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee("Bob", "Hess", 25, 50)
    my_company.add_employee(employee2)

    employee3 = CommisionEmployee("Mary", "Hess", 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()


main()
