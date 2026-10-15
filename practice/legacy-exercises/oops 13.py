
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printdetails(self):
        print(f"the name is {self.fname} {self.lname} ")
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self ,string):
        print("setting now...")
        names =string.split("@")[0]
        self.fname =names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


sparsh =Employee("sparsh","saxena")
arvind = Employee("arvind","saxena")

print(sparsh.email)

sparsh.fname = "spaarsh"
print(sparsh.fname)

sparsh.email = "this.that@gmail.com"
print(sparsh.email)



del sparsh.email
print(sparsh.email)