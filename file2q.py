# WAF that replace all the occurences of "java" with "python"
with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")    
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)