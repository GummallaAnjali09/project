class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

try:
    emp = Employee("Anjali", 20)
    print(emp.salary)
except AttributeError:
    print("The field you're trying to access doesn't exist.")
finally:
    print("End of the program.")
