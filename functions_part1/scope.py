#scopes
#where our variables can be accessed
#in any function when we create a variables created in functions are scoped in that function!

instructor = "colt" ###global scope

def say_hello():
    return f'Hello {instructor}'
print(say_hello())

def say_hi():
    instructor = "jover" ### this variable is only available on this function
    return f'Hello {instructor}'
print(say_hi())

print(instructor) # if i commented out the global scoped variable instructor i will have : NameError: name 'instructor' is not defined

'''
Global 
'''

total = 0

def increment():
    global total # if i want to manipulate a global variable inside my function which has an exisiting value,
                  ## i need to tell python its "global" before i manipulate it
    total += 1
    return total
print(increment())

'''
nonlocal - lets us modify a parent;s variable in a child (aka nested)function
'''

def outer():
    count = 0
    def inner(): #child function
        nonlocal count ### you are telling python that im manipulating the count on the parent function (outer())
        count += 1
        return count
    return inner()