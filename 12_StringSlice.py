#-------------------STRING SLICING-----------------------------
fruit = "Mango"
print(fruit[0:5]) #O/P -> Mango

#Negative String Slicing -> Try to calculate negative index by deducting from length of str.
#Here in this case,we are calculating fruit(names[0:-3]) as fruit(names[0:len(fruit)-3]) -> (fruit[0:2])
print(fruit[0:-3]) #O/P -> Ma

print(fruit[-3:-2]) #O/P -> n
print(fruit[:]) #O/P -> Mango


names ="John,Mary"
#Calculate length of string
print(len(names)) 
print(names[0:2])