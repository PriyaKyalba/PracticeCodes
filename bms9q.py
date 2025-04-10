# Write a python program to accept numbers from the user till he enters “-1”. Print
# the multiplication table of each number accepted.
num = 0
while num != -1:
    num = int(input("Enter a number (-1 to exit): "))
    if num == -1:
        break
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()