class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.__employee_id=employee_id
        self.__salary=float(salary) if salary is not None else 0.0
    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self, employee_id):
        self.__employee_id=employee_id

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary=float(salary)

    def display(self):
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ${self.get_salary()}")

    def __del__(self):
        super().__del__()

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department=department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language=programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
print("--- Python OOP Project: Employee Management System ---")

while True:
    
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice=input("Enter your choice: ").strip()

    if choice=="1":
        name=input("Enter Name: ").strip()
        age=int(input("Enter Age: ").strip())
        person_obj=Person(name, age)
        print(f"Person created with name: {person_obj.name} and age: {person_obj.age}.")
        print("\n--- Choose another operation ---")

    elif choice=="2":
        name=input("Enter Name: ").strip()
        age=int(input("Enter Age: ").strip())
        emp_id=input("Enter Employee ID: ").strip()
        salary=float(input("Enter Salary: ").strip())
        employee_obj=Employee(name, age, emp_id, salary)
        print(f"Employee created with name: {employee_obj.name}, age: {employee_obj.age}, ID: {employee_obj.get_employee_id()}, and salary: ${employee_obj.get_salary():.1f}.")
        print("\n--- Choose another operation ---")

    elif choice=="3":
        name=input("Enter Name: ").strip()
        age=int(input("Enter Age: ").strip())
        emp_id=input("Enter Employee ID: ").strip()
        salary=float(input("Enter Salary: ").strip())
        dept=input("Enter Department: ").strip()
        manager_obj=Manager(name, age, emp_id, salary, dept)
        print(f"Manager created with name: {manager_obj.name}, age: {manager_obj.age}, ID: {manager_obj.get_employee_id()}, salary: ${manager_obj.get_salary():.1f}, and department: {manager_obj.department}.")
        print("\n--- Choose another operation ---")

    elif choice=="4":
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        sub_choice=input("Enter your choice: ").strip()
    elif choice=="5":
        print("Exiting the system. All resources have been freed!")
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice. Please try again.") 