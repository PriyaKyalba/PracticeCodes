#WAP to compute distance between two points taking input from the user
x1 = int(input("enter x1:"))
y1 = int(input("enter y1:"))

x2 = int(input("enter x2:"))
y2 = int(input("enter y2:"))

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(distance)