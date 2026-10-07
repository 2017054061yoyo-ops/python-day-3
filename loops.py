# 2 kinds of loops 1. while loops 2. for loops
#while loop - you don't know how many times its going to happen
#risk of creating a infinate loop, 2 ways to avoid infinate loop: 1. make a condition that can be false 2. use the break keyword
#For loop - when you know the amount of times

borrow_sweater = input ("can I borrow your sweater?")
while borrow_sweater != "Yes": 
    borrow_sweater = input ("can I borrow your sweater?")
    if borrow_sweater == "Yes":
        print("Thank You!")
        break 
    else: 
        print("ohno!")


#Blask off
# Create a countdown before a spaceship lauches
count = 10
while count >= 1:
    print (count)
    count = count -1

print ("Blast off!")
    