class Student:
    @staticmethod #decorator, no need to add self in the ()
    def college():
        return "BMSCE"

    def __init__(self, name , phy , chem , math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math
        print("adding data in database..")
    def avg(self):
        avg = (self.phy + self.chem + self.math) / 3
        return avg
    


st1 = Student("Priya",67,87,56)
print(st1.name,st1.phy,st1.chem,st1.math)
st1.avg()
st1.college()

st2 = Student("karthik",90,88,87)
print(st2.name,st2.phy,st2.chem,st2.math)
st2.avg()
st2.college()