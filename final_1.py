# main script for grocery program

import os
import csv
import pandas as pd
import grocery_fun

# opens folder with function module
# os.chdir("final")

# gives list of dictionaries
grocery = "grocery2.csv"
with open (grocery, "r") as file:
    dict = csv.DictReader(file)
    grocery_dict = [row for row in dict]

# defines aisles variable
aisles = [item["Aisle"] for item in grocery_dict]
aisles = list(set(aisles))

cart = []

###

# welcomes user and explains program
print("Welcome to the Digital Grocery Store!")
print("\nIf you've ever wanted to visualize your grocery trip before you did the real thing, you've come to the right place!")
print("To shop at the Grocery Store, just select which aisles to enter, choose which items to buy, and repeat until you've completed your list.")

# asks for user input wheter to begin
begin = input("\nWould you like to begin? \nEnter 'yes' or 'no':\n")

print("\n")

# continues or closes program based on user input
if begin == "yes":
    print("Ok, now entering the Grocery Store. \nWelcome!")

# elif prevents else from running after if
elif begin == "no":
    print("Ok, now exiting the Grocery Store. \nBye bye!") 
    exit()

else:
    print("Invalid entry, entering the Grocery Store by default!")

### 

print("\nThese are the Grocery Store aisles:\n", aisles)

# asks for user input for aisle to enter
aisles_name = input("\nEnter the name of the aisle you'd like to enter:\n") 
incorrect = 0

# checks for aisle
items = [item["Item"] for item in grocery_dict if item["Aisle"] == aisles_name]
items = list(set(items))
# print(items)

# lists items in aisle
if items:
    print(f"\nThese are the items in the {aisles_name} aisle:\n", items)

# checks for aisle after incorrect entry 
while aisles_name not in aisles:
    print("\nInvalid entry, try again.") 
    incorrect += 1
    if incorrect == 3:
        print("\nThree invalid entries, do you want to keep shopping?")
        aisles_con = input("Enter 'yes' or 'no':\n")
        if aisles_con == "no":
            print("\nOk, now exiting the Grocery Store. \nBye bye!")
            exit()
        elif aisles_con == "yes":
            print("\nOk, continuing shopping! \nJust remember to enter the exact name of the aisle you'd like to enter.")
        else:
            print("\nInvalid entry, continuing shopping by default! \nJust remember to enter the exact name of the aisle you'd like to enter.")
            incorrect = 0  # resets incorrect count
    aisles_name = input("\nEnter the name of the aisle you'd like to enter:\n")

    # checks for aisle after correct entry
    if aisles_name in aisles:
        items = [item["Item"] for item in grocery_dict if item["Aisle"] == aisles_name]
        items = list(set(items))
        print(f"\nThese are the items in the {aisles_name} aisle:\n", items)

###

# asks for user input for item to add
items_name = input("\nEnter the item you'd like to add:\n") 
incorrect = 0 

# checks for item
add = [item["Item"] for item in grocery_dict if item["Item"] == items_name]
add = list(set(add))
# print(add)

# lists items in aisle
if items:
    cart.append(items_name)
    print("\nThese are the items in your cart:\n", cart)

# checks for item after incorrect entry 
while items_name not in items:
    print("\nInvalid entry, try again.") 
    incorrect += 1
    if incorrect == 3:
        print("\nThree invalid entries, do you want to keep shopping?")
        items_con = input("Enter 'yes' or 'no':\n")
        if items_con == "no":
            print("\nOk, now exiting the Grocery Store. \nBye bye!")
            exit()
        elif items_con == "yes":
            print("\nOk, continuing shopping! \nJust remember to enter the exact name of the item you want.")
        else:
            print("\nInvalid entry, continuing shopping by default! \nJust remember to enter the exact name of the item you want.")
            incorrect = 0  # resets incorrect count
    items_name = input("\nEnter the item you'd like to add:\n")

# checks for item after correct entry
    if items:
        cart.append(items_name)
        print("\nThese are the items in your cart:\n", cart)

### 

grocery_con = input("\nWould you like to continue shopping? \nEnter 'yes' or 'no':\n") 

if grocery_con == "no": 
    print("\nOk, now proceeding to checkout.") 
    grocery_fun.checkout()

while grocery_con == "yes":
    print("\nOk, returning to aisle menu.") 
    grocery_fun.shop()

    grocery_con = input("\nWould you like to continue shopping? \nEnter 'yes' or 'no':\n")
    if grocery_con == "no": 
        print("\nOk, now proceeding to checkout.")
        break

grocery_fun.checkout()
# when grocery_fun.shop() is used instead of checkout, list appends