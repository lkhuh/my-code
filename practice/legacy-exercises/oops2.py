class Employee:
    no_of_leaves = 5
    pass

harry = Employee()
harry = Employee()


harry.name = "harry"
harry.salary = 344
harry.role = "Instructor"

print(Employee.no_of_leaves)
Employee.no_of_leaves = 6
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
harry.no_of_leaves = 6
print(harry.no_of_leaves)
