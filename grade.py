marks = int(input("enter your marks: "))

if(marks>=90):
    print("A")
elif(marks<90 and marks>=80):
    print("B")
elif(marks<80 and marks>=70):
    print("C")  
elif(marks<70):
    print("D")
else:
    print("FAIL")       
