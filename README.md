# Employee Management System

## Overview

This project is a Python Object-Oriented Programming (OOP) program for managing people, employees, and managers.

The program uses classes, inheritance, encapsulation, constructors, methods, and a menu-driven interface.

## Features

- Create a Person with a name and age.
- Create an Employee with employee ID and salary.
- Create a Manager with department information.
- Store employee ID and salary using private attributes.
- Use getter and setter methods to access and update private data.
- Use inheritance between Person, Employee, and Manager.
- Use a simple command-line menu to interact with the program.

## Class Structure

### Person

The `Person` class is the base class.

Attributes:
- `name`
- `age`

### Employee

The `Employee` class inherits from `Person`.

Additional attributes:
- `__employee_id`
- `__salary`

Methods include:
- `get_employee_id()`
- `set_employee_id()`
- `get_salary()`
- `set_salary()`
- `display()`

### Manager

The `Manager` class inherits from `Employee`.

Additional attribute:
- `department`

The `display()` method extends the employee details by displaying the department.

### Developer

The `Developer` class inherits from `Employee`.

Additional attribute:
- `programming_language`

The `display()` method extends the employee details by displaying the programming language.

## OOP Concepts Used

### Encapsulation

Employee ID and salary are stored as private attributes using double underscores.

```python
self.__employee_id
self.__salary
```

Getter and setter methods are used to access and modify these values.

### Inheritance

The project demonstrates multilevel inheritance:

```text
Person
  |
Employee
  |
Manager
  |
Developer
```

More precisely, `Manager` and `Developer` both inherit directly from `Employee`.

```text
        Person
          |
       Employee
       /      \
  Manager   Developer
```

### Constructors

Each class uses the `__init__()` constructor to initialize its attributes.

### Method Overriding

`Manager` and `Developer` override the `display()` method from `Employee` and add their own information.

### Super()

The `super()` function is used to call methods and constructors from the parent class.

## Menu Options

When the program starts, it displays the following menu:

```text
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

### Option 1: Create a Person

Takes the person's name and age and creates a `Person` object.

### Option 2: Create an Employee

Takes:
- Name
- Age
- Employee ID
- Salary

and creates an `Employee` object.

### Option 3: Create a Manager

Takes:
- Name
- Age
- Employee ID
- Salary
- Department

and creates a `Manager` object.

### Option 4: Show Details

Provides options for displaying details of the created objects.

### Option 5: Exit

Exits the program.

## Example

Example employee creation:

```text
Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000

Employee created with name: Jane Smith, age: 28, ID: E123, and salary: $50000.0.
```

Example manager creation:

```text
Enter Name: Alice Johnson
Enter Age: 40
Enter Employee ID: M456
Enter Salary: 80000
Enter Department: 4

Manager created with name: Alice Johnson, age: 40, ID: M456, salary: $80000.0, and department: 4.
```

## Requirements

- Python 3.x

No external Python libraries are required.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run the Python file:

```bash
python "OOP Wrapper.py"
```

4. Follow the instructions displayed in the terminal.

## Project Purpose

The main purpose of this project is to demonstrate fundamental Python OOP concepts through a practical Employee Management System.

## Project Files

- `OOP Wrapper.py` — Main Python program.
- `output(2).csv` — Sample program output.
- `README.md` — Project documentation.
