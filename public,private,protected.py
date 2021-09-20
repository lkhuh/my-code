class Employee:
    no_of_leaves = 4
    _protected = 6
    __private = 7
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdet(self):
        return f"the name is {self.name} salary is {self.salary} role is {self.role}"

karan = Employee("karan",444,"employee")
shubam = Employee("shubam",777,"instructor")

emp = Employee("sparsh",673,"nothing")
print(emp._Employee__private)