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
    #
    # @classmethod
    # def from_str(cls,string):
    #     return cls(*string.split("-"))

    # @staticmethod
    # def printgood (string):
    #     print("thisisgood"+ string,end="")
    #     return ("sparsh")




    def __init__(self, aname, arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def sparsh(self):
        return f"The name is {self.name}  role is {self.role} salary is {self.salary}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    #
    # @classmethod
    # def from_str(cls,string):
    #     return cls(*string.split("-"))

    # @staticmethod
    # def printgood (string):
    #     print("thisisgood"+ string,end="")
    #     return ("sparsh")


class Player(Employee):
    def __init__(self, aname, arole, asalary, languages):
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.language = languages

    def printprog(self):
        return f"the programmer's name is {self.name} salary is {self.salary} role is {self.role}, languages are {self.language}"




harry = Employee("harry","student",344)
rohan = Employee("rohan","teacher",455)
shubam = Player("shubam",444,"programmer","python")
karan = Player("karan",665,"programmer","python")
print(karan.no_of_leaves)