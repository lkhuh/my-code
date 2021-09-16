class Employee:
    no_of_leaves = 4
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdet(self):
        return f"the name is {self.name} salary is {self.salary} role is {self.role}"

class Player:
    def __init__(self,anames,agame):
        self.name = anames
        self.game = agame

    def printplayerdetails(self):
        return f"player name is {self.name} player plays {self.game}"





class Coolemployee(Employee,Player):
    language = "c++"
    def printlanguage(self):
        print(self.language)
    def printdetailsofcoolemployee(self):
        return f"the name is {self.name} , salary is {self.salary} role is {self.role} languages are {self.language}"


karan = Employee("karan",444,"employee")
shubam = Employee("shubam",777,"instructor")
harry = Player("harry",["PUBG"])
larry = Player("LARRY",["FREE FIRE"])
arvind = Coolemployee("arvind",8889,"allrounder",)

print(arvind.printdetailsofcoolemployee())

