# Write a program which takes a word and a letter as input and returns the number of occurences of
# that letter in the word.
string = input("Enter a word: ")
letter = input("Enter a letter: ")
count = 0
for char in string:
    if char == letter:
        count += 1  
print("The letter", letter, "occurs", count, "times in the word", string)