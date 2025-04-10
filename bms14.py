# Write a Python program to iterate through a string and check whether a particular character is
# present or not. If present, true should be printed otherwise, false should be printed.
string = input("Enter a string: ")
char_to_check = input("Enter a character to check: ")

if string.find(char_to_check) != -1:
    print("True")
else:
    print("False")

#-1 means not found



# found = False
# for char in string:
#     if char == char_to_check:
#         found = True
#         break
# if found:
#     print("True")
# else:
#     print("False")

