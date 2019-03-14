'''
EXERCISE 1
product(2,2) # 4
product(2,-2) # -4
'''
def product(a,b):
    return a * b
product(2,2)
print("#######break#######")
'''
EXERCISE 2
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None
print("#######break#######")
'''BONUS ADVANCED VERSION:

Here's a more advanced solution that involves error handling, which we have not covered yet.  It eliminates the need to check to see if num is a valid index in the list. We cover this in the debugging section, but I thought you may want to see if now.
'''
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
print("#######break#######")

'''
write a function called last_element. This function takes in one parameter(a list) and returns the last value in the list
it should return None if the list is empty
last_element([1,2,3]) # 3
last_element([]) # None
'''
def last_element(num):
    if num:
        return num[-1]
    return None
print(last_element('hello'))
print("#######break#######")
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a,b):
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return "First is greater"
    return "Second is greater"
print(number_compare(1,1))
print(number_compare(3,100))
print(number_compare(3,4))
print("#######break#######")
'''
In my solution, I use the built-in count()  to count the number of times letter  appears in string . 
I also downcase both string  and letter  to make it case-insensitive (you could also upcase both instead)

'''
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
print(single_letter_count('jay jover', 'j'))

'''
I used a dictionary comprehension. For each letter in the input string, 
I make the key the letter itself ("a" for example), and the corresponding value is the result of running count() of that letter in the string.
'''
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}
print(multiple_letter_count('hello'))
print("#######break#######")
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
print("#######break#######")
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''
def is_palindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
# #### SOLUTION BY THE TRAINOR###
##### Here's the simpler version that doesn't ignore whitespace.  I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.
#
# def is_palindrome(string):
#     return string == string[::-1]
####The Bonus Version:
# For the more advanced version that ignores whitespace, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings ("").  I save the result to a new variable I call stripped .  Then, I simply check if stripped is a palindrome, using the same logic I did in the previous solution.
#
# def is_palindrome(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]
print("#######break#######")

'''
Write a function called frequency. This function accepts a list and a search_term(this will always be a primitive value) 
and returns the number of times the search_term appears in the list
'''
def frequency(collection, searchTerm):
    return collection.count(searchTerm)
print("#######break#######")

'''
Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the 
product of all even numbers in the list
'''
'''In my solution, I start with a variable called total.
Since we're working with multiplication, I start it off as 1.
Then I iterate through the list, checking if each num is cleanly divisible by 2
If it is, I multiply total by the number
At the end, after the loop finishes, I return total
'''
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
print("######break######")
'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    return string.capitalize()
print(capitalize("hello"))
print("#######break######")
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
def compact():
    return [val for val in l if val]
'''
Without a list comprehension
I make a list to store all truthy values
I iterate over each value in the list
I check if the value is truthy (using a simple if val )
If the value is truthy, add it to the truthy_vals  list
return truthy_vals  at the end
'''
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals
print("#######break######")

# flesh out intersection pleaseeeee
# intersection([1,2,3], [2,3,4]) #2,3
def intersection(l1, l2): ###manual looping
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
def intersection(l1, l2): #### list comprehension
    return [val for val in l1 if val in l2]
def intersection(list1, list2): #### using set
    return [val for val in set(list1) & set(list2)]


print("####break###")
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

'''
Here's my solution that doesn't use a list comprehension:

I have two lists, to hold the true and false values
I loop through the list, calling fn  with each value in the list
If the result is True, I append the value to the trues  list
Otherwise, I append the value to the falses  list
At the end I return a list that contains both the trues  and falses  lists
'''
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]


'''List Comprehension Version
Using a list comprehension, you can get this function down to a single line.  It's definitely a tradeoff though.  It's much short but also more difficult to understand.  It's a fine balance between brevity and readability.
'''
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


'''Another Solution
This solution was submitted by a student named Jonathan.  Thanks, Jonathan!
'''
def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]
