#----------------STRINGS-----------------------------
#Anything that is enclosed within single or double quotation mark is called as string.
name = "Debjit"
friend = "Rohan"
print(name,"is a good friend of",friend)

#String is like an array of characters . We can access part of string by usig its index which starts from 0.
print(name[0])
print(name[1])

for character in name: #Accessing each character using for loop
    print("Character is",character)
    
sent = "Hi Harry,\"How are you\"?" #If we want to use quotation marks in between a sentence, we use backslash("\") to highlight it otherwise it might show you an error.
print(sent)

#Printing multiline sentences
multi = '''Save Water: "Water is a precious resource that is essential for life. Conserving water is crucial for maintaining our environment and ensuring that future generations have access to clean water. 
Simple actions like fixing leaks, using water-efficient appliances, and collecting rainwater can significantly reduce water waste." 

The Importance of Healthy Eating: "Healthy eating is vital for maintaining overall health and well-being. A balanced diet rich in fruits, vegetables, whole grains, and lean proteins can help prevent chronic diseases and promote a healthy weight. 
Making informed food choices and being mindful of portion sizes are key components of a healthy lifestyle."'''

print(multi)
    

