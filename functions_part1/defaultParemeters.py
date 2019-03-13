def exponent(num, power):
    return num ** power
print(exponent(2,3))


def exponent(num, power=2):  #### so if you dont pass a power, the default parameter of power is 2
    return num ** power
print(exponent(2))

def show_information(firstname="jay", is_driver=False):
    if firstname == "jay" and is_driver:
        return "welcome back driver jay"
    elif firstname == "jay":
        return "i thought you were a driver...."
    return f"Hello {firstname}"
print(show_information()) # it will fall to elif return
print(show_information(is_driver=True)) #it will fall to if return
print(show_information('other')) # last return "Hello other

### why have default params?
#### allow you to be more defensive
#### avoids errors with incorrect parameters
#### more readable examples!

### what can default parameters be?
###anything! functions,lists,dictionaries,strings,booleans - all of the above!

def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b


