class Employee:
    no_of_leaves = 7
    def __init__(self,asalary ,arole,acharachter):
        self.salary = asalary
        self.role = arole
        self.charachter = acharachter

def sparsh(self):
    return f"The name is {self.name} salary role is {self.role} charrachter is {self.charachter}"

harry = Employee(454,"student","foddie")
print(harry.salary)
