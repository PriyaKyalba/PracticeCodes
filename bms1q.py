#write a program that asks the user how many fibonaccinnumbers to generate and then generate them
num = int(input("enter number:"))
n1,n2=0,1
print(n1,n2)
for var in range(2,num):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3