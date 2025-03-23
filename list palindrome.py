list = [1,2,3,2,1]
list_copy = list.copy()
list_copy.reverse()

if(list_copy==list):
    print("palindrome")
else:
    print("not a palindrome")   