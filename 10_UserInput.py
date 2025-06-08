#---------------------TAKING USER INPUT------------------------
#We can take user input directly by the input() function.This gives a return value as string/character.
a=input("Enter your name : ")
print(a)

x=input("Enter first number : ")
y=input("Enter second number : ")
print(x+y)
#Input function returns the value as string.Hence we have to typecast whenever required to another datatype. 
p=int(input("Enter first number : "))
q=int(input("Enter second number : "))
print(p+q)