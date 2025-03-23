#WAF to print the elements of the list(list is a parameter)
nums = [1,4,8,69,0,87,45]
places = ["goa","madras","nainital","pondi"]
def print_el(list):
    for val in list:
        print(val,end = " ")
       
print_el(places)  
print_el(nums)