class Employee:
    no_of_leaves = 8



    def __init__(self):
        self.name = "harry"
        self.salary = 345
        self.role = "programmer"


    def __add__(self, other):
        return self.salary + other.salary


    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"THE name is {self.name} salary is {self.salary} role is {self.role} "
    def printdetails(self):
        return f"AND THE name is {self.name} salary is {self.salary} role is {self.role} "
    def __str__(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role} "



emp1= Employee()


print(emp1.name)


