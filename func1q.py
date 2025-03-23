# WAF to print length of a list(list is a parameter)
nums = [1,4,8,69,0,87,45]
places = ["goa","madras","nainital","pondi"]
#function defination
def print_len(list):
    print(len(list))
    return len(list)
#function calling
print_len(nums)
print_len(places)