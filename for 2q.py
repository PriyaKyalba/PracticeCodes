"""search for a number X in this tuple using loop
[1,4,9,16,25,36,49,64,81,100]"""
num= [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter x: "))
for val in num:
    if(val==x):
        print(x,"FOUND")
        break
    else:
        print("finding..")    
print("end")