age = int(input("enter your age: "))

#suppose age > 80 are not eligible to drive

if(age>=18):
    if(age>=80):
        print("can not drive")
    else:
        print(" Yes,you can drive")   
else:
    print("CANNOT DRIVE")        