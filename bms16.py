# Write a program which takes a word and a number as input and returns the character at that
# position.
string = input("Enter a word: ")
num = int(input("Enter a number: "))
if num < len(string):
    print("The character at position", num, "is:", string[num])
else:
    print("The number is out of range.")