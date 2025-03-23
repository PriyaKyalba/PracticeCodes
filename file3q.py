#search if the word "learning" exists in the file or not
with open("practice.txt","r")as f:
    data = f.read()
    if(data.find("learning")!= -1):
         print("FOUND")
    else:
        print("NOT FOUND")