# WAP to find the factorial of first n natural numnbers
n = int(input("enter n: "))
fact = 1
for i in range (1,n+1):
    fact*=i
    i+=1
print("factorial of n numbers are: ",fact)