# WAF to find in which line of the file  does the word "learning" occur first 
# print -1 if the word is not found
def check_for_line():
    word ="learning"
    data = True
    line_no = 1
    with open ("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1    
    return -1        

check_for_line()