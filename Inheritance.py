class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id)
        self.salary = salary
    def display_info(self):
        super().display_info()
        print(f"Employee Type: Full Time")
        print(f"Salary: ETB{self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def display_info(self):
        super().display_info()
        print(f"Employee Type: Part-Time")
        print(f"Houry Rate: ETB{self.hourly_rate}")
        print(f"Hours Worked: {self.hours_worked}")
        
        
full_time_employee = FullTimeEmployee("Alice", 101, 60000)
part_time_employee = PartTimeEmployee("Bob", 102, 20, 25)


print("Full-Time Employee Details: ")
full_time_employee.display_info()

print("\nPart_Time Employee Details: ")
part_time_employee.display_info()
        