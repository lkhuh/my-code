class Employee:
    no_of_leaves = 7
    def __init__(self, aname , arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def sparsh(self):
            return f"The name is {self.name}  role is {self.role} salary is {self.salary}"

    @classmethod
    def change_leaves(cls,newleaves):
     cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))



harry = Employee("harry","student",344)
rohan = Employee("rohan","teacher",455)
karan = Employee.from_str("karan-instructor-466")
# harry.change_leaves
print(karan.salary)