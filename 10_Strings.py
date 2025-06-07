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
    

