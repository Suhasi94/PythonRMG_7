
class Employee:
    fname = "steve"         # class variables
    lname = "jobs"

    def __init__(self, fname, lname):
        self.fname = fname          # object/instance variables
        self.lname = lname
        print(fname,lname)

    def display(self,name,surname):
        self.name = name
        self.surname = surname
        print(self.fname, self.lname)
        print(name,surname)
    def details(self):
        print(self.name,self.surname)


e1 = Employee("tata", "birla")
e2 = Employee("Mukesh", "Ambani")

e1.display("suhasini","kattimani")
e1.details()

print(Employee.fname)






