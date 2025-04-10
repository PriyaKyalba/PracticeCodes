# Write a program to print all the letters from sen1 that also appear in sen2. sen1= North America, 
# sen2= South America.
sen1 = "North America"
sen2 = "South America"
letters = set(sen1.lower()) & set(sen2.lower()) #lowercase+split into unique set of characters like {'a', 'n'}
print("Letters in both sentences:", letters)
 

# write a program to print all the words from sen1 that also appear in sen2. sen1= North America,
# sen2= South America.
sen1 = "North America"
sen2 = "South America"
words = set(sen1.lower().split()) & set(sen2.lower().split())#lowercase+split into unique set of words like {'north', 'south', 'america'}
print("Words in both sentences:", words)
