class Cars:
    def __init__(self): # self means the object is being created by us
        print("adding cars data in database.")
    model = "BMW"
    color = "black"

car1 = Cars()
print(car1.model)
print(car1.color)


class Student():
    college = "BMSCE"  #data which is common for all objects 
    def __init__(self,name,marks,section):
        self.name = name         #self. mtlb us object ka value is not same for all
        self.marks = marks
        self.section = section
        print("adding student data..")

st1 = Student("Priya",95,"C")
print(st1.name,st1.section,st1.marks,st1.college)

st2 = Student("Karthik",99,"A")
print(st2.name,st2.marks,st2.section,st2.college)
