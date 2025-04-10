# Write a program to check if a string is a paindrome or not.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
string = input("Enter a string: ")
for i in string:
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

#[::-1] reverses the string