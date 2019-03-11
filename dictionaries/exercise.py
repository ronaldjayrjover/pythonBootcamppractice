'''
Exercise

the food variable will store a randomly chosen food string like "gummy bear" or "morning bun"
Some of these items are in the bakery_stock dictionary, and some are not.

Your task is to simply print out a string depending on if food is a value  in bakery_stock
If food is contained in bakery_stock print out a string that states how many items are left:
3 left if food is tofee cookie or 1 left if food is "morning bun" etc
If food is not contained in the bakery_stock, print out "We dont make that"
'''

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


# YOUR CODE GOES BELOW:
#SOLUTION
#Section 14, Lecture 129
####Bakery Dictionary Exercise Solution
############REMEMBER, WE HAVE TO USE FORMAT() RATHER THAN F-STRINGS IN THE UDEMY CODE EDITOR!

#The following code is common to all solutions:


###Solution using IN
###In the last video, we saw how to use in to test if a value is contained in a dictionary:

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

#####Solution using get()
#We can do the same thing using get() and storing the result to a variable.  The variable will either contain the corresponding value from the dictionary OR None.  We can write a simple conditional check:

quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")