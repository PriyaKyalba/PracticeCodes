#write a program that asks the user how many fibonacci numbers to generate and then generate them
num = int(input("enter number:"))
n1=0
n2=1
print(n1)
print(n2)
for i in range (1,num):
    n3 = n1+n2
    print(n3)
    n1=n2
    n2=n3