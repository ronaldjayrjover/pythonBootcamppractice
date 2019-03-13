#what is a function - a process for executing a task. it can accept input and return an output
#why use functons - stay DRY - Dont Repeat Yourself. celanup and precent code duplication.
# "Abstratc away" code for other users - imagine if you had to rewrite the "print()" function for every code


colors = ['red', 'orange', 'yellow']
colors.append('violet')
print(colors)

#def name_of_function():
    #

def say_hi():
    print('Hi!')
say_hi()

def sing_happy_birthday():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday to You")
sing_happy_birthday()

def make_noise():
    print("THE CROWD GOES WILD")
make_noise()

'''
Returning Values from Functions
'''
def print_square_of_7():
    print(7**2)
print_square_of_7()

def square_of_7():
    return 7**2
result = square_of_7()
print(result)
'''
return exits the function
return outputs whatever value is placed after the return keyword
return Pops the function off the call stack

'''