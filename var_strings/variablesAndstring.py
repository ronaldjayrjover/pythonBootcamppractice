'''variables in python
'''


#variables reassignment

x = 1
y = x

print(y)

a, b, c = 5, 10, 15

print(a)
print(b)
print(c)

#restrictions #stylistics
   #cats
   #_cats


xa = 100
niyahaha = 1
print(xa + niyahaha)

##### Dynamic Typing ####

awesomeness = True
print(awesomeness) ## True /  Bolean

awesomeness = "a dog"
print(awesomeness) # string

awesomeness = None
print(awesomeness) # None

awesomeness = 22 / 7
print(awesomeness) # float

##### What is None ####
None #represent the idea of Nothingness

name = "daisy"
age = 30
child = None

print(child) ; print(type(child))

### Declaring Strings by '' or ""

firstString = "a hat"
secString = 'a hat'
print(firstString); print(type(firstString))
print(secString); print(type(secString))


### String Escape Characters/Sequences

new_line = "hello \n world"
print(new_line)

backslashdouble = "this is a backslash \\"
print(backslashdouble)

    ### from the exercise
# Set the message variable equal to any string containing a new-line escape sequence
message = "Hello \n goodbye"

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!

mountains = "/\\/\\/\\"


# Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "My cat said \"meow\""



### String Concatenation

string1 = "your"
string2 = "face"
string3 = string1 + " "  + string2
print(string3)


username = "thecat"
print("Hello there, " + username)

thename = "ice"
thename += " water"
print(thename)


### Formatting Strings
### interpolate variables

xyz = 10
formatted1 = f"ive told you {xyz} times already" #python3
print(formatted1)
formatted2 = "ive told you {} times already".format(10) ##python2
print(formatted2)
formatted3 = "ive told you %d times already" % (xyz) ## old way : deprecated
print(formatted3)
formatted4 = f"your guess of {xyz + 1}, is right"
print(formatted4)

     ####from test
first = "ronald"
last = "ehem"

formatted = "First Name: {}, Last Name: {} ".format(first, last)

### String Index
name = "chuck"
print(name[0])

### converting data types

#sample
decimal = 1.2222
integer = int(decimal)
print(integer)

firstlist = [1, 2, 3]
convertedlist = str(firstlist)
print(convertedlist)


