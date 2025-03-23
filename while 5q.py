"""search for a number X in this tuple using loop
[1,4,9,16,25,36,49,64,81,100]"""
x = int(input("enter x: "))
num = (1,4,9,16,25,36,49,64,81,100)
i=0
while i<len(num):
    if(num[i]==x):
        print("FOUND",i)
    else:
        print("finding...")    
    i +=1   


