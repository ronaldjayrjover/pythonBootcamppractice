def square(num):
    return num ** 2

print(square(4))
print(square(8))


def sing_happy_birthday(name):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday to You")
sing_happy_birthday("charlie")
sing_happy_birthday("chaplin")

def add(a,b):
    return a+b
print(add(2,3))

def multiply(first, second):
    return first * second
print(multiply(5,5))

####Naming Parameters
def print_full_name(firstname, surname):
    return(f"Your full name is {firstname} {surname}")

'''
parameter is a variable in a method definition
when a method is called, the arguments are the data you pass into the method's parameter
parameter is variable in the declaration of function
argument is the actual value of this variable that gets pass to function 

def square(num):  ##### num is parameter
    return num ** 2

square(4) ###### 4 is the argument
'''

def divide(num1, num2):
    return num1/num2
print(divide(2,5))

def yell(string):
    #return string.upper() + "!" #concatenation
    #return "{}!".format(string.upper()) # string format()
    return f"{string.upper()} !" # f_string
print(yell("hello"))
