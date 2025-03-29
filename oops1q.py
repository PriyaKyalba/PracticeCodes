#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print th avg
class Student():
    def __init__(self,name,phy,chem,math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math
        print("adding data in database..")
    def avg(self):
        avg = (self.phy + self.chem + self.math)/3
        print(avg)

st1 = Student("Priya",67,87,56)
print(st1.name,st1.phy,st1.chem,st1.math)
st1.avg()

st2 = Student("karthik",90,88,87)
print(st2.name,st2.phy,st2.chem,st2.math)
st2.avg()