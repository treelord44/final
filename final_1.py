# opens operating system so we can access files
import os
os.getcwd()
os.chdir("final")

# opens file so we can use functions
import grocery 

# if I change the directory after importing the module I need, can I still use the module?
os.getcwd()
os.chdir("final_data")
os.listdir()

###

# welcomes user and explains program
print("Welcome to the Digital Grocery Store!")
print("\nIf you've ever wanted to visualize your grocery trip before you did the real thing, you've come to the right place!")
print("To shop at the Grocery Store, just select which aisles to enter, choose which items to buy, and repeat until you've completed your list.")

print("\n")

#variable
begin = input("Would you like to begin? \nEnter 'yes' or 'no':\n")
aisles = os.listdir()

print("\n")

# continues or closes program based on user response
if begin == "yes":
    print("Ok, now entering the Grocery Store. \nWelcome!")
# elif prevents else from running after if
elif begin == "no": 
    print("Ok, now exiting the Grocery Store. \nBye bye!") 
    exit()
else:
    print("Invalid entry, entering the Grocery Store by default!")

### 

# I wanna use an API to collect data for aisles, but I can't install requests >:[

print("\n")
print("These are the Grocery Store aisles:\n", aisles)

print("\n")
aisles_enter = input("Enter the file name of the aisle you'd like to enter: ") 
path = os.path.exists(aisles_enter)

while path == True:
    print("alrighty")
    break

while path == False:
    print("sorry bud")
    break



###

# lists 
# can webscrape for data instead, then make it into lists/aisles
# what if I made the differnet aisles into separate files O_O
# so users can import the speific aisle/file they want to select items from

##fruits = ["banana, mango, apple, blueberry, papaya"]
##vegetables = ["lettuce, broccoli, carrot, cabbage, radish"]
##grains = ["rice, oats, quinoa, wheat, barley"]

# select what list you want to select from
# select what items you want from the list 
# find the prices

##aisle = input("Choose which aisle to select from: ") 
##items = input("Choose what items you would like from the aisle: ") 
##items_more = input("Would you like to select more items?: ") 


##grocery_list = [] 
##grocery_list.append(input) 