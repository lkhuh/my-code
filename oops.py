class Sparsh:
    
    def printdetails(self):
        return f"name is {self.name},role is {self.role},salary is {self.salary}"
    
harry = Sparsh()
rohan = Sparsh()

harry.salary = 123
harry.role = ("student")
harry.name = ("harry")

print(harry.printdetails())
print(harry.salary)