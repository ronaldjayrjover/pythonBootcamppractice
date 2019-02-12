'''
loop through number 1-20
for 4 and 13, print "x is unlucky"
for even numbers, print "x is even"
for odd numbers, print "x is odd"
'''

for x in range(1,21):
    if x == 4 or x == 13:
        print(f"{x} is unlucky")
    elif x % 2 == 0: ### modulo(%) means if there is no remainder then its even
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

###refactor/simplified below
for x in range(1,21):
    if x == 4 or x == 13:
        state = "unlucky"
    elif x % 2 == 0: ### modulo(%) means if there is no remainder then its even
        state = "even"
    else:
        state = "odd"
    print(f"{x} is {state}")