# module with functions for grocery program

import os
import csv
import pandas as pd

# opens folder with this module
os.chdir("final")

# gives list of dictionaries
grocery = "grocery2.csv"
with open (grocery, "r") as file:
    dict = csv.DictReader(file)
    grocery_dict = [row for row in dict]

# defines aisles variable
aisles = [item["Aisle"] for item in grocery_dict]
aisles = list(set(aisles))

cart = []

####################

def shop():
    """
    Allows user to choose aisle to enter and items to add
    """
    print("\nThese are the Grocery Store aisles:\n", aisles)

    # asks for user input
    aisles_name = input("\nEnter the name of the aisle you'd like to enter:\n") 
    incorrect = 0

    # checks for aisle
    items = [item["Item"] for item in grocery_dict if item["Aisle"] == aisles_name]
    items = list(set(items))

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

    # asks for user input
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

####################

def checkout():
    """
    Gives user total cost of items added
    """
    total_cost = 0

    print("\nCheckout Summary:")
    for item_name in cart:
        item_info = next(item for item in grocery_dict if item["Item"] == item_name)
        item_price = float(item_info["Price"])
        print(f"{item_name}: ${item_price:.2f}")
        total_cost += item_price

    print("\nTotal Cost: ${:.2f}".format(total_cost))
    print("\nThank you for visiting the Digital Grocery Store!")
