# Write a Python program to calculate the length of a string without using built-in function.
# The length of a string is the number of characters in it.
string = input("Enter a string: ")
length = 0
for char in string:
    length += 1
print("The length of the string is:", length)